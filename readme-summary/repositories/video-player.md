# video-player

**Summary**

*Living Paintings* is an experimental project that converts original static paintings into animated sequences. Each scene originates from a physical artwork where internal rules for light, motion, and structure encode implied motions (e.g., lighting gradients simulate ray tracing). The repository contains six example scenes:

1. **Aerial Coastline & Crystal City** – Uses gradient lighting to enhance perceived depth.
2. **Jungle Undergrowth & Small Dinosaurs** – Encodes depth through overlap and occlusion, revealing traversal paths rather than explicit motion vectors.
3. **Maiasaurs with Their Nest** – Poses encode balance and orientation, producing low‑movement dynamics.
4. **White Horse in Blue Motion** – Depicts a single dominant motion vector for smooth animation.
5. **Alien Rock Structures on a Lavender World** – Primarily extends camera movement through fixed spatial geometry.
6. **Cliffside Dragon** – Uses hinge points and counter‑torque to generate stable rotational motion.

The README explains the underlying mathematical framework:

- **Paintings as Constraint Sheaves**: The canvas space \(X\) maps each subregion \(U \subseteq X\) to a set of valid physical interpretations \(F(U)\). A sheaf condition (local agreement and gluing) ensures coherent global interpretation.
- **Animation as Global Section Selection**: Animation selects one consistent global interpretation from the sheaf and extends it over time using a motion operator \(T\).
- **Built‑In Optics**: Painting cues such as specular smear, bloom gradients, and fading distances act like optical components baked into the paint.
- **Reducing Ambiguity While Painting**: Specific painterly choices (clear axis orientation, uneven stride, mass imbalance) shrink the set of possible global interpretations.

**Key Claim:** Animation does not invent motion; it unfolds constraints already encoded in the painting, treating each artwork as a partially‑specified physics model rather than a static image.

**KEYWORDS:** video player, animation from paintings, constraint sheaves, optical encoding, implicit motion, experimental art.
