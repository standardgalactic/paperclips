# forge-template

**Summary**

The *Forge Standard Library* (foundry-rs/forge-std) provides a suite of utility contracts and helper functions designed to simplify development with the **Forge** and **Foundry** toolchains. Its primary goals are:

1. **Error Handling** – `stdError` offers a comprehensive mapping of compiler‑builtin error codes, making it easier to use Forge’s `expectRevert` cheatcode for robust testing.
2. **Storage Manipulation** – `stdStorage` wraps the powerful `record` and `accesses` cheatcodes, enabling automatic detection and writing to storage slots without prior knowledge of layout constraints (e.g., handling packed storage variables safely).
3. **Cheatcode Wrappers** – `stdCheats` provides higher‑level wrappers around miscellaneous cheatcodes like `prank`/`hoax`, facilitating safer ETH transfers during testing.
4. **Assertion Enhancements** – Extends the assertion capabilities of the DSTest library for more expressive test conditions.
5. **Logging Improvements** – Offers a Forge‑compatible logging interface (`console.log`) that decodes log values, with an alternative `console.sol` for Hardhat compatibility.

The library is installed via Forge’s cheatcode system and integrates directly with the Foundry development environment, enhancing both testing efficiency and developer UX. It supports multiple licensing options (MIT or Apache 2.0).

**KEYWORDS:**
forge standard library
Forge Foundry
stdError contract
stdStorage wrapper
stdCheats utility
assertion enhancements
console logging
MIT license
Apache 2.0 license
