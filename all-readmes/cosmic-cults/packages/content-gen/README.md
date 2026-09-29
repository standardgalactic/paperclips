# @cosmic-cults/content-gen

AI-powered 3D asset generation for Cosmic Cults using Meshy API.

## Overview

This package generates 3D GLB models for game assets (units, buildings, leaders) using Meshy AI's text-to-3D API. Each faction has custom prompts tailored to their theme:

- **Crimson Covenant**: Blood rituals, demonic power, gothic horror
- **Order of the Deep**: Lovecraftian ocean horror, fish-human hybrids, sunken cities
- **Void Seekers**: Cosmic horror, dimensional rifts, reality manipulation

## Setup

1. Ensure `.env` file exists in repository root:
```bash
# .env
MESHY_API_KEY=msy_your_api_key_here
```

2. Install dependencies:
```bash
pnpm install
```

## Usage

### List Available Assets

See all assets that can be generated:

```bash
pnpm --filter @cosmic-cults/content-gen gen:list
```

Filter by faction or type:

```bash
# List only Crimson Covenant assets
pnpm --filter @cosmic-cults/content-gen gen:list --faction crimson-covenant

# List only unit assets
pnpm --filter @cosmic-cults/content-gen gen:list --type unit
```

### Generate 3D Models

#### Dry Run (Preview Only)

See what would be generated without calling the API:

```bash
pnpm --filter @cosmic-cults/content-gen gen:models:dry
```

#### Generate Preview Models

Generate low-poly preview models (faster, cheaper):

```bash
# Generate all assets (WARNING: 50+ assets, will cost credits!)
pnpm --filter @cosmic-cults/content-gen gen:models

# Generate specific faction
pnpm --filter @cosmic-cults/content-gen gen:models --faction crimson-covenant

# Generate specific type
pnpm --filter @cosmic-cults/content-gen gen:models --type unit

# Generate specific asset
pnpm --filter @cosmic-cults/content-gen gen:models --id blood_knight --type unit
```

#### Generate Refined Models

Generate high-quality refined models with PBR textures (slower, more expensive):

```bash
# Generate refined models for specific faction
pnpm --filter @cosmic-cults/content-gen gen:models:refined --faction void-seekers

# Generate refined model for specific asset
pnpm --filter @cosmic-cults/content-gen gen:models --refine --id abyssal_horror --type unit
```

### CLI Options

```bash
tsx src/cli.ts models [options]

Options:
  -f, --faction <faction>         Generate for specific faction
                                  (crimson-covenant, order-of-the-deep, void-seekers)
  -t, --type <type>               Generate specific asset type
                                  (unit, building, leader)
  -i, --id <id>                   Generate specific asset by ID
  -r, --refine                    Also generate refined high-quality models
  -d, --dry-run                   Show what would be generated without calling API
  -c, --max-concurrent <number>   Maximum concurrent API calls (default: 3)
```

## Output Structure

Generated models are saved to `generated/models/`:

```
generated/models/
├── blood_knight/
│   ├── manifest.json       # Asset metadata and task state
│   ├── preview.glb         # Low-poly preview model
│   └── refined.glb         # High-quality refined model (if --refine used)
├── crimson_temple/
│   ├── manifest.json
│   └── preview.glb
└── ...
```

## Asset Prompts

Prompts are organized by faction in `src/game/prompts/`:

- `crimson-covenant.ts` - Blood cult units, buildings, leaders
- `order-of-the-deep.ts` - Lovecraftian ocean horror assets
- `void-seekers.ts` - Cosmic void and reality manipulation assets

Each prompt is carefully crafted to:
- Describe the asset's appearance in detail
- Include art style keywords (dark fantasy, Lovecraftian, etc.)
- Specify pose mode (A-pose for characters)
- Match the faction's theme and aesthetic

## Cost Considerations

Meshy API charges per task:
- **Text-to-3D Preview**: ~$0.10 per model
- **Text-to-3D Refine**: ~$0.20 per model

Generating all 50+ assets:
- Preview only: ~$5-10
- Preview + Refine: ~$15-20

**Recommendation**: Start with dry runs and specific assets to test prompts before generating everything.

## Extending

### Add New Assets

1. Add the asset type to `@cosmic-cults/types` package
2. Add prompts to appropriate faction file in `src/game/prompts/`
3. The manifest builder will automatically pick it up

### Customize Generation

Edit `src/game/manifest-builder.ts` to change:
- Target poly count
- Art style (realistic vs sculpture)
- Topology (quad vs triangle)
- Symmetry mode
- PBR settings

## Integration with Game

Generated GLB models can be loaded in the game:

```typescript
import { assetLoader } from '@cosmic-cults/assets';
import type { UnitType } from '@cosmic-cults/types';

// Load generated model
const model = await assetLoader.loadModel('blood_knight' as UnitType);
```

Place generated GLB files in `public/models/` directory and update the asset manifest.

## Troubleshooting

### API Key Not Found

Ensure `.env` file exists in repository root with:
```bash
MESHY_API_KEY=msy_your_actual_key
```

### Rate Limiting

Meshy API has rate limits. The generator:
- Processes assets in batches of 3 (configurable with `-c`)
- Waits 5 seconds between batches
- Retries on rate limit errors (max 3 retries with exponential backoff)

### Task Failures

If generation fails:
1. Check the error message in console output
2. Review the failed asset's manifest.json
3. Adjust prompts if needed
4. Retry specific assets with `--id` flag

## Examples

```bash
# Test a single asset first
pnpm --filter @cosmic-cults/content-gen gen:models --id blood_acolyte --type unit

# Generate all Crimson Covenant units
pnpm --filter @cosmic-cults/content-gen gen:models --faction crimson-covenant --type unit

# Generate all buildings with refinement
pnpm --filter @cosmic-cults/content-gen gen:models --type building --refine

# Preview what would be generated for all assets
pnpm --filter @cosmic-cults/content-gen gen:models:dry
```

## Future Enhancements

- [ ] Animation generation via Meshy rigging API
- [ ] Retexturing support for style variations
- [ ] Batch download of existing GLB models
- [ ] Integration with asset manifest in `@cosmic-cults/assets`
- [ ] Quality validation and poly count optimization
- [ ] Automatic LOD generation
