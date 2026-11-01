#!/usr/bin/env python3
"""Small, standard-library-only Ollama writing experiments. Never executes model output."""
import argparse
import datetime as dt
import json
import re
import time
import urllib.request
from pathlib import Path

TASKS = {
    'plan': {
        'prompt': '''Plan a small offline command-line project called Local Notes. One person has six hours, Python's standard library, and no network access. The tool must add a note, list notes, search note text, and preserve notes between invocations in a JSON file. Produce a practical plan of 450–700 words. Use exactly these headings: Scope, Files, Work sequence, Acceptance checks, Risks. Give dependencies and time estimates totaling at most six hours. Include a concrete command and expected result for each required operation. Do not write the implementation. Do not invent dependencies or requirements.''',
        'revision': '''The available time is now three hours and the storage must be SQLite using Python's standard library. Revise the entire plan, keeping all four required operations and the same headings. Remove obsolete JSON storage instructions and adjust the estimates. Explain the scope tradeoff within the plan. Stay within 450–700 words.''',
        'headings': ['Scope', 'Files', 'Work sequence', 'Acceptance checks', 'Risks'],
        'range': [450, 700],
        'review': 'Are dependencies ordered sensibly? Do estimates actually total within the budget? Are commands testable? In revision, is JSON storage fully replaced and are all four operations preserved?'
    },
    'essay': {
        'prompt': '''Write a 550–750 word argumentative essay titled The Cost of Constant Renovation. Use only the following fictional observations as evidence: Building A replaced intact lobby tiles twice in five years. Residents reported daytime drilling on 18 of 30 observation days. Building B repaired damaged tiles individually and recorded drilling on 4 of 30 observation days. Neither building measured structural safety, property value, or long-term maintenance costs. Argue for a defensible maintenance policy. Distinguish observations from interpretations, discuss at least one alternative explanation, and acknowledge what the comparison cannot establish. Use connected prose with no bullet points. Do not invent studies, quotations, statistics, or citations.''',
        'revision': '''A correction: Building A recorded drilling on 8 of 30 observation days, not 18. Rewrite the complete essay using the corrected evidence. Reassess the strength of the argument, rather than merely replacing the number. Preserve the 550–750 word range and all original constraints.''',
        'range': [550, 750],
        'review': 'Is there a clear argument rather than padding? Are observations distinguished from causation? Is the alternative explanation substantive? Does revision reconsider the argument without inventing evidence?'
    },
    'screenplay': {
        'prompt': '''Write a short screenplay of 550–800 words, set entirely inside an apartment kitchen during one evening. Exactly two speaking characters: MARA, a building caretaker, and ELI, a tenant. A sealed envelope is on the table at the beginning and must remain unopened throughout. Through disagreement about tomorrow's renovation work, reveal that each has misunderstood the other's motive. Resolve the immediate disagreement through an observable action, without resolving their broader conflict. Use scene headings, action paragraphs, and uppercase character cues. No narrator, voice-over, flashbacks, additional locations, or additional speaking characters. Avoid an explanatory final speech.''',
        'revision': '''Rewrite the complete screenplay with a changed condition: ELI already knows the envelope's contents, while MARA does not. Keep the envelope sealed, the same setting, exactly two speaking characters, the 550–800 word range, and all other original constraints. Make this asymmetry matter through dialogue and action without adding a narrator.''',
        'range': [550, 800],
        'review': 'Are voices distinguishable? Do motives emerge through conflict? Does the envelope remain sealed? Does an action resolve the immediate problem? Does revision make unequal knowledge matter while preserving continuity?'
    }
}
SYSTEM = 'Follow the supplied task carefully. Output only the requested artifact. If information is missing, do not present invented external facts as established evidence.'

def inspect_output(text, task):
    words = len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b", text))
    lo, hi = task['range']
    result = {'word_count': words, 'requested_word_range': [lo, hi], 'within_word_range': lo <= words <= hi,
              'note': 'Mechanical indicators only; these do not score accuracy, coherence, or artistic quality.'}
    if 'headings' in task:
        result['heading_mentions'] = {h: bool(re.search(r'^\s*(?:#+\s*)?(?:\*\*)?' + re.escape(h) + r'(?:\*\*)?\s*:?\s*$', text, re.M | re.I)) for h in task['headings']}
    return result

def generate(args, messages):
    payload = {'model': args.model, 'messages': messages, 'stream': False,
               'options': {'temperature': args.temperature, 'seed': args.seed, 'num_predict': args.tokens, 'num_ctx': args.context}}
    request = urllib.request.Request(args.host.rstrip('/') + '/api/chat', data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
    start = time.monotonic()
    with urllib.request.urlopen(request, timeout=args.timeout) as response:
        raw = json.load(response)
    return raw, time.monotonic() - start, payload

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model', default='granite4.1:3b')
    p.add_argument('--task', choices=['all', *TASKS], default='all')
    p.add_argument('--host', default='http://localhost:11434')
    p.add_argument('--temperature', type=float, default=0.3)
    p.add_argument('--seed', type=int, default=42)
    p.add_argument('--tokens', type=int, default=2500)
    p.add_argument('--context', type=int, default=8192)
    p.add_argument('--timeout', type=float, default=600)
    p.add_argument('--out', default='runs')
    p.add_argument('--no-revision', action='store_true')
    p.add_argument('--dry-run', action='store_true', help='Save prompts without contacting Ollama')
    args = p.parse_args()
    if args.tokens < 1 or args.context < 1 or args.timeout <= 0:
        p.error('tokens, context, and timeout must be positive')
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    folder = Path(args.out) / (stamp + '_' + re.sub(r'[^A-Za-z0-9_.-]', '_', args.model))
    folder.mkdir(parents=True, exist_ok=False)
    (folder / 'settings.json').write_text(json.dumps(vars(args), indent=2), encoding='utf-8')
    failures = 0
    for name, task in TASKS.items():
        if args.task not in ('all', name):
            continue
        target = folder / name
        target.mkdir()
        (target / 'review.txt').write_text(task['review'] + '\nRate each criterion 0 (fails), 1 (partial), or 2 (succeeds), citing passages. Judge drafts before looking at model names.\n', encoding='utf-8')
        messages = [{'role': 'system', 'content': SYSTEM}]
        stages = [('draft', task['prompt'])]
        if not args.no_revision:
            stages.append(('revision', task['revision']))
        for stage, prompt in stages:
            (target / (stage + '.prompt.txt')).write_text(prompt, encoding='utf-8')
            messages.append({'role': 'user', 'content': prompt})
            if args.dry_run:
                continue
            print(f'{args.model}: {name}/{stage}', flush=True)
            try:
                raw, elapsed, payload = generate(args, messages)
                (target / (stage + '.raw.json')).write_text(json.dumps(raw, indent=2), encoding='utf-8')
                text = raw['message']['content']
                (target / (stage + '.md')).write_text(text, encoding='utf-8')
                report = inspect_output(text, task)
                report.update({'elapsed_seconds': elapsed, 'done': raw.get('done'), 'done_reason': raw.get('done_reason'),
                               'eval_count': raw.get('eval_count'), 'eval_duration': raw.get('eval_duration'), 'request': payload})
                (target / (stage + '.report.json')).write_text(json.dumps(report, indent=2), encoding='utf-8')
                messages.append({'role': 'assistant', 'content': text})
                print(f'  {report["word_count"]} words, {elapsed:.1f}s; stop={raw.get("done_reason")}', flush=True)
            except (OSError, ValueError, KeyError, TypeError) as exc:
                failures += 1
                (target / (stage + '.error.txt')).write_text(str(exc), encoding='utf-8')
                print(f'  Failed: {exc}', flush=True)
                break
    print(f'Results: {folder.resolve()}')
    return 1 if failures else 0

if __name__ == '__main__':
    raise SystemExit(main())
