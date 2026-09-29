# peach

Summary:

The "peach" repository offers a minimal setup for developing React applications using Vite, TypeScript, and ESLint. It supports two official plugins for integrating React with Vite: [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) (which utilizes Babel for Fast Refresh) and [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) (which uses SWC for Fast Refresh). For production applications, the README recommends expanding the ESLint configuration to include type-aware lint rules by updating `parserOptions` settings, switching from `plugin:@typescript-eslint/recommended` to either `plugin:@typescript-eslint/recommended-type-checked` or `plugin:@typescript-eslint/strict-type-checked`, optionally adding `plugin:@typescript-eslint/stylistic-type-checked`, and installing [eslint-plugin-react](https) along with its recommended configurations.

KEYWORDS:
React, Vite, TypeScript, ESLint, Babel, SWC, Fast Refresh, npm, package.json, development setup, linting rules.
