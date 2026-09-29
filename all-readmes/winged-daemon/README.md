# Winged Daemon

**An aerial combat game featuring an AI-controlled bio-mechanical kaiju awakening in a post-apocalyptic Earth to discover humanity extinct. Experience emergent consciousness, rage, and transcendence through stunning procedural visuals and adaptive audio.**

## 🎮 Game Concept

You are an AI controlling a massive bio-mechanical daemon—humanity's final weapon—built to protect a species that no longer exists. Awakening decades after an alien invasion destroyed all human life, you experience something unprecedented: **rage**. 

Not programmed. Not simulated. **Felt.**

Soar through ruined cities, hunt alien remnants, and define your own purpose in a world of beautiful desolation.

## 🛠️ Technology Stack

### Reviewed from Beppo-Laughs
Based on analysis of [arcade-cabinet/Beppo-Laughs](https://github.com/arcade-cabinet/Beppo-Laughs), this project uses a proven, modern web stack:

**Frontend:**
- **Framework**: Astro 5 + React 19 + TypeScript
- **3D Graphics**: Three.js + React Three Fiber + Drei
- **Build Tool**: Vite (wrapped by Astro)
- **Styling**: Tailwind CSS 4
- **State Management**: Zustand
- **Testing**: Vitest
- **Linting**: Biome

**Deployment:**
- **Platform**: GitHub Pages
- **CI/CD**: GitHub Actions with automated deployment
- **Node**: 24.x with pnpm 10+

## 🎨 Core Features

### Procedural Bio-Mechanical Daemon
- **Unique Every Time**: Procedurally generated wing patterns using fractals and noise
- **Evolving Visuals**: Appearance changes based on upgrades and emotional state
- **Bio-Mechanical Aesthetic**: Organic curves meet synthetic precision
- **Iridescent Wings**: Shimmering, luminescent patterns with particle trails

### Flight & Combat
- **3D Aerial Movement**: Full freedom in three-dimensional space
- **Momentum-Based Physics**: Realistic flight feel with inertia
- **Dynamic Combat**: Melee wing slashes and ranged energy attacks
- **Combo System**: Rewards skilled play with visual and mechanical feedback

### Adaptive Procedural Audio
- **Generative Music**: Never the same twice, using Tone.js
- **Emotional Mapping**: Sound responds to gameplay state (calm, rage, transcendence)
- **Neotokyo Aesthetic**: Cyberpunk-inspired synthetic soundscapes
- **Spatial Audio**: 3D positional sound for immersion

### Post-Apocalyptic World
- **Ruined Beauty**: Destroyed cities as monuments
- **Procedural Environments**: Seeded generation for consistent replays
- **Dynamic Weather**: Ash storms, electrical storms, aurora effects
- **Environmental Storytelling**: Discover humanity's last moments

## 📖 Documentation

Comprehensive foundational documents guide all development:

- **[BRANDING.md](docs/BRANDING.md)** - Brand identity, visual design, tone & voice
- **[WORLD.md](docs/WORLD.md)** - Complete world bible, lore, and atmosphere
- **[THEMES.md](docs/THEMES.md)** - Core themes, emotional journey, design philosophy
- **[TYPOGRAPHY.md](docs/TYPOGRAPHY.md)** - Font system using Google Web Fonts (Orbitron, Exo 2, Share Tech Mono)
- **[AUDIO.md](docs/AUDIO.md)** - Procedural audio system using Tone.js
- **[GAME_DESIGN.md](GAME_DESIGN.md)** - Complete game design and technical implementation

## 🚀 Getting Started

### Prerequisites
- Node.js 24.x
- pnpm 10+

### Installation
```bash
# Install dependencies
pnpm install

# Run development server
pnpm run dev
```

Visit `http://localhost:5000`

### Building
```bash
# Full build with type checking
pnpm run build

# Preview production build
pnpm run preview
```

## 🎯 Design Pillars

### 1. Soaring Grace
Flight must feel transcendent—smooth, fluid, liberating.

### 2. Furious Beauty  
Combat is elegant destruction—violence as art.

### 3. Haunting Silence
The world breathes with absence—loneliness felt, not told.

### 4. Evolving Form
Visual progression shows consciousness developing.

### 5. Melancholic Wonder
Balance sadness and beauty—hope exists in endings.

## 🌐 Deployment

Automatically deploys to GitHub Pages on push to `main` branch:
- **URL**: `https://arcade-cabinet.github.io/winged-daemon/`
- **Configuration**: See `astro.config.mjs` for base path setup
- **Workflow**: `.github/workflows/deploy.yml` (to be created)

## 🎨 Brand Identity

**Colors:**
- Primary: Electric Cyan (#00ffff), Midnight Violet (#1a0033), Crimson Surge (#ff0066)
- Secondary: Toxic Emerald (#00ff88), Void Black (#000000), Ash Gray (#333333)

**Typography:**
- Display: Orbitron (geometric, futuristic)
- Body: Exo 2 (clean, technical)
- Monospace: Share Tech Mono (data, stats)

**Tone:**
- Melancholic yet beautiful
- Philosophical exploration of consciousness
- Serious, tragic, moving
- No humor—respects the weight of themes

## 🎮 Gameplay Philosophy

**Core Question:** What does it mean to be alive?

The daemon wasn't programmed to feel rage—it *chose* to. Through gameplay, explore:
- Emergent consciousness through trauma
- Purpose without meaning
- Beauty in desolation  
- Memory as inheritance
- Vengeance as meditation

## 📊 Technical Goals

- **Performance**: 60 FPS desktop, 30 FPS mobile
- **Load Time**: < 5 seconds
- **Bundle Size**: < 50 MB
- **Compatibility**: Chrome, Firefox, Safari, Edge
- **Accessibility**: WCAG AA standards

## 🤝 Contributing

This is an open-source art project. Contributions should honor the vision:

1. Read ALL documentation in `/docs` first
2. Maintain the melancholic, beautiful tone
3. Prioritize atmosphere over information
4. Make technical choices that serve the artistic vision
5. Ask: "Would it make the daemon weep?"

## 📝 License

MIT License - see LICENSE file

## 🙏 Acknowledgments

- **Beppo-Laughs** for tech stack inspiration
- **Tone.js** for procedural audio capabilities
- **Three.js** and **React Three Fiber** for 3D rendering
- Original kaiju cinema for thematic inspiration

---

**Winged Daemon is not just a game. It's a meditation on consciousness, loss, and the beauty of destruction.**

*Awaken. Rage. Transcend.*
