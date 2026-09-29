# Crystal-GNN

**Summary of the Process**

1. **Initial Setup (First MD Dataset)**
   - The first dataset was computed with a basic INCAR configuration:
     ```
     SMASS = 1.0
     LWAVE = F
     LCHARG = F
     ISPIN = 1
     ISTART = 1
     ICHARG = 1
     NPAR = 2
     KPAR = 4
     ```
   - Parsing resulted in **1 parsing error** due to some high-energy configurations being removed by the property filter. After fixing this, a second MD run was performed with:
     - `NSW: 4000` (reduced from 7000)  
     - Energy convergence criteria (`EDIFF = 1E-06`) and temperature start (`TEBEG = 500`) were kept.
   - The final parsing completed without errors, yielding **238000 data points**.

2. **Second MD Dataset**
   - For the second dataset, a more stable configuration was used:
     ```
     POTIM = 5.00
     NSW    = 4000
     TEBEG  = 500
     MDALGO = 3 (Langevin thermostat)
     ```
   - Parsing initially encountered **6 parsing errors**, indicating non-convergence in some calculations. To address this, the number of steps (`NSW`) was reduced from 7000 to 4000.
   - After re-running these six datasets with the adjusted configuration:
     - All six converged successfully (no more parsing errors).
   - The final successful parsing yielded **402000 data points**.

**Conclusion**
Both datasets were processed by first identifying and correcting initial convergence issues, then adjusting INCAR parameters to improve stability. The second dataset's reduced `NSW` helped achieve a higher success rate in both XML parsing and MD simulation completion.
