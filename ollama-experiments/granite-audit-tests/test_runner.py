import json, threading, unittest
from http.server import HTTPServer, BaseHTTPRequestHandler
import audit
class Tests(unittest.TestCase):
 def test_answer_key(self):
  self.assertEqual([audit.expected(c)['actual_sum'] for c in audit.CASES],[120,105,150,135,90,100])
 def test_correct(self):
  self.assertTrue(audit.grade(json.dumps([audit.expected(c) for c in audit.CASES]),audit.CASES)['all_correct'])
 def test_wrong_sign_and_boolean(self):
  rows=[audit.expected(c) for c in audit.CASES];rows[1]['exceeds_budget']=True;rows[2]['remainder']=30
  score=audit.grade(json.dumps(rows),audit.CASES)
  self.assertFalse(score['cases'][1]['fields']['exceeds_budget']);self.assertFalse(score['cases'][2]['fields']['remainder'])
 def test_missing_duplicate_extra(self):
  rows=[audit.expected(c) for c in audit.CASES]
  for changed in (rows[:-1],rows+[rows[0]],rows+[dict(rows[0],id='Z')]): self.assertFalse(audit.grade(json.dumps(changed),audit.CASES)['all_correct'])
 def test_types_and_malformed(self):
  row=audit.expected(audit.CASES[0]);row['claim_correct']=1
  self.assertFalse(audit.grade(json.dumps([row]),audit.CASES[:1])['all_correct'])
  self.assertFalse(audit.grade('invalid',audit.CASES)['parse_ok'])
 def test_http(self):
  class H(BaseHTTPRequestHandler):
   def do_POST(self):
    self.server.received=json.loads(self.rfile.read(int(self.headers['Content-Length'])))
    self.send_response(200);self.end_headers();self.wfile.write(json.dumps({'message':{'content':'[]'},'done':True}).encode())
   def log_message(self,*args): pass
  server=HTTPServer(('127.0.0.1',0),H);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
  try:
   payload,raw,elapsed=audit.request(f'http://127.0.0.1:{server.server_port}','mock','audit',42,.3,3000,10)
   self.assertEqual(raw['message']['content'],'[]');self.assertEqual(len(server.received['messages']),1)
  finally: server.shutdown();server.server_close();thread.join()
if __name__=='__main__': unittest.main()
