# preprocessor-loader

Summary:

The preprocessor-loader is a webpack loader designed for conditional compilation of HTML, TypeScript (TS), and CSS files using comment directives reminiscent of C/C++ preprocessors. It enables developers to create platform-specific builds, such as distinguishing between desktop and mobile environments. By integrating with webpack configurations, it processes input files like the example HTML snippet, outputting only the relevant content based on specified conditions (e.g., `PLATFORM == 'mobile'`). The loader supports multiple key/value pairs for conditional compilation, allowing customization of which code blocks are included or excluded from the final build.

KEYWORDS: preprocessor-loader, webpack, conditional compilation, HTML, TypeScript, CSS, platform-specific builds, comment directives, C/C++ preprocessor language.
