# @cosmic-cults/ai

AI systems with GenAI-powered decision making for Cosmic Cults.

## Architecture

```
┌─────────────────────────────────────────┐
│         TypeScript Dev Layer            │
├─────────────────────────────────────────┤
│  AIController (High-level management)   │
│  ↓                                      │
│  GenAI Engine (Strategic decisions)     │
│  ↓                                      │
│  WASM Bridge (Type-safe interface)      │
└─────────────────┬───────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│         Rust Execution Layer            │
├─────────────────────────────────────────┤
│  game-ai crate (Performance-critical)   │
│  - Pathfinding execution                │
│  - Behavior trees                       │
│  - Combat calculations                  │
└─────────────────────────────────────────┘
```

## Features

### GenAI Decision Engine
- Uses GPT-4o-mini for strategic AI decisions
- Context-aware tactical analysis
- Faction-specific behavior modeling
- Confidence scoring and reasoning

### TypeScript Controller
- Entity management and lifecycle
- Batch decision processing
- Cooldown management
- Difficulty scaling

### WASM Bridge
- Type-safe Rust ↔ TypeScript communication
- Batch command execution
- State synchronization
- Performance optimization

## Usage

```typescript
import { aiController } from '@cosmic-cults/ai';

// Initialize AI system
await aiController.initialize();

// Register AI-controlled unit
aiController.registerEntity({
  id: 1,
  faction: 'void-seekers',
  type: 'cultist',
  position: { q: 0, r: 0 },
  health: 100,
  maxHealth: 100
});

// Update AI (called each frame)
await aiController.updateEntity(1, {
  nearbyEnemies: [
    { type: 'blood_warrior', position: { q: 2, r: 1 }, distance: 3 }
  ],
  nearbyAllies: [],
  resources: { sanity: 50, blood: 30, knowledge: 20 },
  currentTurn: 5,
  phase: 'exploration'
});

// Set difficulty
aiController.setDifficulty('hard');

// Get strategic analysis (debugging)
const analysis = await aiController.getAnalysis(1, context);
console.log(analysis);
```

## GenAI Configuration

Set your OpenAI API key:

```bash
export OPENAI_API_KEY=sk-...
```

Or configure in your app:

```typescript
import { openai } from '@ai-sdk/openai';

const customModel = openai('gpt-4o', {
  apiKey: process.env.OPENAI_API_KEY
});
```

## Decision Types

- `move`: Move to a position
- `attack`: Attack an enemy
- `defend`: Defensive stance
- `gather`: Collect resources
- `build`: Construct buildings
- `retreat`: Fall back to safety
- `ritual`: Perform faction ritual

## Performance

- **Batch updates**: Process multiple entities per frame
- **Caching**: Similar situations reuse decisions
- **Cooldowns**: Prevent excessive API calls (1s per entity)
- **Fallback**: Rule-based decisions when GenAI fails

## Integration with Rust

The WASM bridge communicates with the `game-ai` Rust crate:

```rust
// Rust side (game-ai/src/lib.rs)
#[wasm_bindgen]
pub fn execute_ai_command(command: WasmAICommand) {
    // Execute command in Bevy ECS
}

#[wasm_bindgen]
pub fn get_ai_state(entity_id: u32) -> WasmAIState {
    // Return current AI state
}
```

## Testing

```bash
pnpm test
```

## Development

```bash
# Type check
pnpm check

# Build
pnpm build
```
