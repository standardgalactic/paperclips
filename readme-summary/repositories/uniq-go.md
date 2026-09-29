# uniq-go

Summary:

The uniq-go repository provides a Go utility package named `uniq` designed to generate common random unique identifiers in three formats: UUID (Universally Unique Identifier), Base32, and variable-length hexadecimal strings. The UUID format is 16 bytes long with 36 characters, Base32 format is 20 bytes long with 32 characters, and the hexadecimal format can be of any length `n`, resulting in `n*2` characters. 

Base32() is highlighted as a superior alternative to UUID() for scenarios where space efficiency and broader filesystem compatibility are needed, offering increased randomness from 2^128 (UUID) to 2^160 (Base32). Additionally, the package includes several convenience commands (`uuid`, `uid32`, `isosec`, `epoch [SECONDS]`, `randhex [COUNT]`) for direct integration into shell scripts.

The project is supported by GoDoc, Go Report Card, and Gocover badges indicating documentation completeness, reporting status, and coverage respectively. It is currently in a mature implementation stage with no evident incompleteness as per the README.

KEYWORDS:
uniq-go package
random identifiers
UUID format
Base32 encoding
Go programming language
unique identifier utilities
