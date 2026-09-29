# DataFitting.jl

Below is a self‑contained Julia example that shows how to use the built‑in components (OffsetSlope, Polynomial, Gaussian, Lorentzian) together with the model fitting workflow described in your note.  The code includes comments so you can see exactly what each step does.

```julia
# ------------------------------------------------------------------
# 1️⃣  Import required packages and set a random seed for reproducibility
# ------------------------------------------------------------------
using Random, Plots, DataFitting, Gnuplot

Random.seed!(0)   # same as MersenneTwister(0) in the note

# ------------------------------------------------------------------
# 2️⃣  Define the data model (1‑D example: offset + two Gaussian peaks)
# ------------------------------------------------------------------
using DataFitting.Components   # contains all built‑in components
using LinearAlgebra            # for @vec, reshape etc.

# Create a domain and add expressions / parameters to the model
x = Domain(1:0.05:10)                     # independent variable

model = Model(
    :offset => 4,                           # fixed offset (will be overwritten by fit!)
    :line1  => DataFitting.Components.Gaussian(1.1,   # Gaussian #1 parameters
                                                4.4, 0.51),
    :line2  => DataFitting.Components.Gaussian(0.52,   # Gaussian #2 parameters
                                                5.5, 1.2)
)

# Add the domain to the model so that it knows how to evaluate expressions
add_dom!(model, x)

# The expression we want to fit is simply the sum of the offset and the two Gaussians.
# (The fixed parameter for :offset will be overwritten by the optimizer.)
add_expr!(model, :(offset + line1 + line2))

# ------------------------------------------------------------------
# 3️⃣  Generate synthetic data with noise
# ------------------------------------------------------------------
rng = MersenneTwister(0)   # same RNG as in the note
noise_amplitude = maximum(model()) * 0.01

data = Measures(
    model() .+ noise_amplitude .* randn(rng, length(model())),   # noisy signal
    noise_amplitude                                          # measurement uncertainty
)

# ------------------------------------------------------------------
# 4️⃣  Fit the model to the data (this will update the free parameters)
# ------------------------------------------------------------------
fit_result = fit!(model, data)   # internally calls prepare! and optimizes

# ------------------------------------------------------------------
# 5️⃣  Plot the results using Gnuplot.jl
# ------------------------------------------------------------------
@gp "set multi layout 2,1" :-
@gp domain(model) data.val data.unc "w yerr tit 'Data'" :-
@gp :- domain(model) model(:line1) .+ model(:offset) "w l tit 'offset + line1'" :-
@gp :- domain(model) model(:line2) .+ model(:offset) "w l tit 'offset + line2'" :-
@gp :- domain(model) model() "w lines tit 'Model' lw 3" :-
@gp :- 2 x[1] (data.val - model()) ./ data.unc fill(1., length(data)) "w yerr tit 'Residuals'"

# ------------------------------------------------------------------
# 6️⃣  Optional: inspect the fitted parameters
# ------------------------------------------------------------------
println("Fitted parameters:")
for (name, param) in fit_result.parameters
    println("$name = $(round(param.value, digits=4))")
end

# The plots will be displayed automatically when you run this script.
```

### How This Example Relates to Your Note

| Step | What It Demonstrates |
|------|---------------------|
| **Component definition** (`OffsetSlope`, `Gaussian`) | Shows how to add built‑in components with the correct constructor signatures. |
| **Fixed vs. free parameters** | The offset parameter is fixed by default (as in your note) and will be overwritten during fitting; you must ensure at least one other parameter remains free for the optimizer to adjust. |
| **`prepare!` call** | After changing any expression, calling `prepare!(model)` recompiles the model before running `fit!`. The example implicitly does this because `fit!` internally calls it. |
| **Plotting residuals & final fit** | Uses Gnuplot.jl to produce a two‑panel figure (data + error bars, fitted curve). This mirrors the “Residuals” plot you described. |

Feel free to adapt the same pattern for 2‑D examples (e.g., using `OffsetSlope` and `Gaussian` with CartesianDomain) or replace Gnuplot with any other Julia plotting package (`Plots.jl`, `PyPlot.jl`, etc.). The key points are:

1. **Component constructors** follow the signatures shown in the module documentation.
2. **Parameter fixing** is handled automatically for components that depend on themselves (e.g., a Gaussian’s width cannot be free if it appears elsewhere).
3. **`prepare!` + `fit!`** ensure the model is recompiled and ready to accept optimizer updates.

Happy modeling!
