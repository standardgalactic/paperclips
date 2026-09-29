# cccForth

Below is an example of how you can extend cccForth by adding a simple “random‑number” primitive. The idea is to define a new word (e.g., **RND**) whose VML code starts with the extension marker **‘z’** and then call it from within `doExt()` so that when the VM sees a ‘z’ command it knows to invoke your custom routine.

### Step‑by‑step guide

1. **Add the word to the prims array**

   In `cccForth.cpp` (or wherever you maintain the primitive list), add an entry for the new word:

   ```cpp
   , { "RND",    "zR" }   // random number generator
   ```

   The first token is the Forth name (`RND`) and the second token is the VML code (`zR`).  
   (If you want to limit it only for a specific board, you can use a #define such as `#ifdef __PIN__` – but here we’ll keep it generic.)

2. **Implement the handler in `doExt()`**

   In the same file, locate the switch statement that processes VML commands:

   ```cpp
   switch (ir) {
       case 'G': pc = doGamePad(ir, pc);           break;
       case 'N': push(micros());                   break; // zN (--n)
       case 'P': pin = pop(); ir = *(pc++);                // Pin operations
               … // existing cases for PIN-IN/OUT/etc.
       case 'W': delay(pop());                     break; // zW (n--)
   ```

   Add a new case for your primitive:

   ```cpp
   case 'R': {
           // Generate a random 31‑bit integer (0 .. 0x7FFFFFFF)
           CELL rand = pop();          // The VM pushes the argument count first.
           push(random(0x100000000)); // Push the result onto the stack.
       } break;
   ```

   Note that `pop()` is used to retrieve any arguments you might pass (e.g., a seed) before pushing the random value. If you want a deterministic “seeded” RNG, you could expose an additional primitive for seeding and then use it inside this block.

3. **Compile / Re‑build**

   After adding the line above, recompile your cccForth project so that the new entry appears in the VM’s lookup table.

4. **Using the new word**

   In a Forth program you can now write:

   ```forth
   10 RND .   \ prints a random number between 0 and 2^31-1
   ```

   The sequence works as follows:
   - `RND` is called.
   - The VM sees the ‘z’ prefix, jumps to `doExt`.
   - It executes the case for `'R'`, calls `random(0x100000000)`, and pushes the result back onto the stack.
   - You can then use standard Forth operators (`.`, etc.) to inspect or print it.

### Full Example

Here’s a minimal snippet that shows how you might extend cccForth with a **RND** word:

```cpp
// prims array entry -------------------------------------------------
, { "RND",    "zR" }   // random number generator

// doExt() handler for the new primitive ---------------------------
switch (ir) {
    case 'G': pc = doGamePad(ir, pc);           break;
    case 'N': push(micros());                   break; // zN (--n)
    case 'P': pin = pop(); ir = *(pc++);                // Pin operations
               … // existing cases for PIN-IN/OUT/etc.
    case 'W': delay(pop());                     break; // zW (n--)
    case 'R': {
           CELL rand = pop();          // argument count is already on top of stack
           push(random(0x100000000)); // push random 31‑bit integer onto stack
       } break;
}
```

### What This Means for You

- **Extensibility**: By prefixing any new Forth word with ‘z’, you tell the VM to invoke a custom handler (`doExt`).  
- **Reusability**: If your extension is useful across multiple projects, consider making it part of a library or adding it in a separate header file so other users can include it.  
- **Safety**: Always ensure that any arguments pushed onto the stack are validated (e.g., non‑negative seeds) before using them in `random()`.

Feel free to adapt this pattern for other primitives—whether they’re hardware‑specific operations, math functions, or anything else you need! If you run into issues with a specific board’s extensions (like the PIN cases), just let me know and we can tailor the handler accordingly.
