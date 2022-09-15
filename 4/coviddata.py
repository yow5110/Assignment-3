# Week 3 Assignment 4
# Make a 2D plot of new COVID19 cases in the UK as a function of day elapsed, using the data below downloaded from WHO. 
# The final plot should have a horizontal dashed line at 100,000, and two vertical lines marking two peak values of your choice. 
# The final plot should also include meaningful labels for both axis.

covid_data_uk = [0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00,
       0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00,
       0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00,
       0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00,
       0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00,
       0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00, 1.00000e+00,
       0.00000e+00, 0.00000e+00, 1.00000e+00, 1.80000e+01, 0.00000e+00,
       1.00000e+00, 0.00000e+00, 0.00000e+00, 3.00000e+00, 1.00000e+00,
       1.00000e+00, 4.00000e+00, 1.00000e+00, 1.00000e+00, 0.00000e+00,
       0.00000e+00, 0.00000e+00, 1.00000e+00, 0.00000e+00, 0.00000e+00,
       0.00000e+00, 2.00000e+00, 0.00000e+00, 6.00000e+00, 2.00000e+00,
       3.00000e+00, 2.00000e+00, 8.00000e+00, 1.30000e+01, 4.00000e+00,
       2.20000e+01, 4.20000e+01, 6.00000e+01, 6.20000e+01, 5.10000e+01,
       8.90000e+01, 7.40000e+01, 5.80000e+01, 1.64000e+02, 2.86000e+02,
       4.28000e+02, 5.22000e+02, 5.26000e+02, 3.71000e+02, 4.53000e+02,
       6.23000e+02, 8.26000e+02, 1.02500e+03, 1.09000e+03, 1.33700e+03,
       1.18300e+03, 1.36100e+03, 2.28900e+03, 2.35300e+03, 2.66600e+03,
       3.03900e+03, 3.15400e+03, 2.77400e+03, 2.81800e+03, 4.19500e+03,
       4.46300e+03, 4.89100e+03, 4.82400e+03, 4.85300e+03, 3.97600e+03,
       3.55600e+03, 5.27300e+03, 5.47700e+03, 5.14600e+03, 4.87500e+03,
       4.32700e+03, 3.58500e+03, 3.50700e+03, 4.20300e+03, 4.33500e+03,
       5.07000e+03, 5.29200e+03, 4.97700e+03, 4.74400e+03, 3.88100e+03,
       4.44100e+03, 4.79500e+03, 5.51700e+03, 5.16700e+03, 4.96100e+03,
       3.75700e+03, 3.47600e+03, 4.73900e+03, 4.71900e+03, 5.43300e+03,
       4.96100e+03, 4.76600e+03, 3.25800e+03, 3.00200e+03, 3.39800e+03,
       3.68600e+03, 3.83200e+03, 3.78700e+03, 3.06400e+03, 2.17000e+03,
       2.33700e+03, 3.61200e+03, 3.41000e+03, 3.33000e+03, 2.63000e+03,
       2.53000e+03, 2.08200e+03, 1.83700e+03, 2.58100e+03, 3.06300e+03,
       2.71900e+03, 2.56700e+03, 2.05700e+03, 1.53200e+03, 1.37300e+03,
       1.62500e+03, 2.07000e+03, 1.82500e+03, 1.75700e+03, 1.53100e+03,
       1.13200e+03, 1.08000e+03, 1.43900e+03, 1.49200e+03, 1.36900e+03,
       1.24900e+03, 1.12300e+03, 8.04000e+02, 7.22000e+02, 1.09900e+03,
       1.16500e+03, 1.19600e+03, 1.01300e+03, 1.05300e+03, 8.86000e+02,
       8.26000e+02, 1.04500e+03, 1.10300e+03, 1.01700e+03, 1.02200e+03,
       9.93000e+02, 6.83000e+02, 6.36000e+02, 8.99000e+02, 8.83000e+02,
       7.77000e+02, 7.26000e+02, 6.66000e+02, 6.53000e+02, 4.49000e+02,
       7.24000e+02, 6.23000e+02, 6.52000e+02, 6.06000e+02, 5.68000e+02,
       3.99000e+02, 5.58000e+02, 7.14000e+02, 6.09000e+02, 7.13000e+02,
       7.22000e+02, 5.68000e+02, 4.59000e+02, 3.66000e+02, 7.40000e+02,
       7.05000e+02, 7.77000e+02, 7.12000e+02, 5.82000e+02, 5.05000e+02,
       4.48000e+02, 8.30000e+02, 7.88000e+02, 8.16000e+02, 8.08000e+02,
       7.74000e+02, 5.30000e+02, 5.63000e+02, 8.69000e+02, 8.56000e+02,
       1.06200e+03, 9.46000e+02, 6.98000e+02, 5.59000e+02, 5.64000e+02,
       1.06000e+03, 1.06600e+03, 1.09200e+03, 1.10500e+03, 9.73000e+02,
       7.10000e+02, 6.27000e+02, 1.49900e+03, 1.37800e+03, 1.24200e+03,
       1.15600e+03, 1.18500e+03, 7.14000e+02, 6.02000e+02, 1.29800e+03,
       1.11600e+03, 1.28200e+03, 1.49800e+03, 1.21800e+03, 8.42000e+02,
       8.31000e+02, 1.30100e+03, 1.27000e+03, 1.38800e+03, 1.59100e+03,
       1.63200e+03, 1.23000e+03, 1.17100e+03, 1.51300e+03, 2.28800e+03,
       3.07700e+03, 3.15200e+03, 3.09200e+03, 2.55100e+03, 2.46500e+03,
       3.93100e+03, 3.37000e+03, 3.36500e+03, 3.62800e+03, 3.32400e+03,
       2.67000e+03, 2.15400e+03, 3.42800e+03, 3.55100e+03, 4.39900e+03,
       4.67500e+03, 4.97300e+03, 4.88900e+03, 5.34000e+03, 5.62700e+03,
       6.44100e+03, 7.09600e+03, 7.68200e+03, 7.31800e+03, 6.81000e+03,
       7.02300e+03, 9.98300e+03, 1.03660e+04, 1.27170e+04, 1.33570e+04,
       1.38540e+04, 1.16670e+04, 1.19530e+04, 1.67530e+04, 1.72500e+04,
       1.85730e+04, 1.84250e+04, 1.58930e+04, 1.26480e+04, 1.22020e+04,
       1.96710e+04, 1.91160e+04, 1.99200e+04, 1.86070e+04, 1.79150e+04,
       1.48820e+04, 1.43110e+04, 2.58720e+04, 2.56130e+04, 2.57140e+04,
       2.34750e+04, 2.16940e+04, 1.64340e+04, 1.58960e+04, 2.68070e+04,
       2.43500e+04, 2.39010e+04, 2.36140e+04, 2.28900e+04, 1.66730e+04,
       1.59700e+04, 3.19250e+04, 2.59430e+04, 2.40270e+04, 2.40620e+04,
       2.36600e+04, 1.87660e+04, 2.02450e+04, 3.15110e+04, 2.77890e+04,
       2.77570e+04, 2.48260e+04, 2.43890e+04, 1.82230e+04, 1.62320e+04,
       2.69510e+04, 2.34870e+04, 2.10800e+04, 1.80410e+04, 1.71000e+04,
       1.25330e+04, 1.18950e+04, 1.90240e+04, 1.66770e+04, 1.68130e+04,
       1.47610e+04, 1.45550e+04, 1.10860e+04, 1.08510e+04, 1.81970e+04,
       1.66840e+04, 1.66760e+04, 1.58600e+04, 1.58340e+04, 1.28930e+04,
       1.37310e+04, 2.15850e+04, 2.10650e+04, 2.19090e+04, 2.29160e+04,
       2.43900e+04, 1.95880e+04, 2.22660e+04, 3.51970e+04, 3.43780e+04,
       3.54270e+04, 3.44380e+04, 3.64190e+04, 2.55900e+04, 3.30660e+04,
       4.81920e+04, 4.64750e+04, 4.29360e+04, 3.23920e+04, 1.44190e+04,
       4.11100e+04, 4.85200e+04, 4.64090e+04, 8.30900e+04, 7.21610e+04,
       5.39460e+04, 3.24820e+04, 6.16540e+04, 5.63350e+04, 7.79720e+04,
       6.66370e+04, 5.87840e+04, 5.31870e+04, 4.81050e+04, 4.00350e+04,
       3.71740e+04, 5.85920e+04, 5.06470e+04, 4.65090e+04, 4.34730e+04,
       4.14510e+04, 3.12490e+04, 2.95920e+04, 4.59580e+04, 4.05260e+04,
       3.59860e+04, 3.25020e+04, 3.03300e+04, 2.23450e+04, 1.75540e+04,
       3.07370e+04, 2.77300e+04, 2.63030e+04, 2.47730e+04, 2.24330e+04,
       1.71670e+04, 1.57830e+04, 2.29720e+04, 2.02660e+04, 1.99140e+04,
       1.84930e+04, 1.63080e+04, 1.23200e+04, 1.16640e+04, 1.61940e+04,
       1.42250e+04, 1.38990e+04, 1.31390e+04, 1.25730e+04, 9.03500e+03,
       8.99400e+03, 1.47350e+04, 1.29410e+04, 1.19420e+04, 1.17940e+04,
       1.07280e+04, 8.31300e+03, 8.09700e+03, 1.16560e+04, 9.76300e+03,
       8.84600e+03, 8.02500e+03, 6.78300e+03, 4.94900e+03, 4.87300e+03,
       7.19200e+03, 6.91900e+03, 6.17200e+03, 5.93700e+03, 5.46700e+03,
       4.62800e+03, 4.41000e+03, 6.89000e+03, 6.48800e+03, 6.25100e+03,
       5.93300e+03, 5.71600e+03, 4.37900e+03, 4.42500e+03, 6.69800e+03,
       5.84900e+03, 5.97600e+03, 5.62300e+03, 5.17600e+03, 4.24600e+03,
       5.38800e+03, 6.45800e+03, 5.48100e+03, 6.22400e+03, 5.61600e+03,
       4.56700e+03, 3.73100e+03, 5.02900e+03, 4.19600e+03, 3.77900e+03,
       3.96700e+03, 3.67400e+03, 2.74700e+03, 2.50600e+03, 2.41300e+03,
       2.74400e+03, 3.31200e+03, 3.25300e+03, 3.14700e+03, 2.95200e+03,
       2.38000e+03, 2.37600e+03, 2.88000e+03, 2.49500e+03, 2.51200e+03,
       2.34500e+03, 2.34700e+03, 1.72200e+03, 2.58400e+03, 2.73800e+03,
       2.54100e+03, 2.70900e+03, 2.40900e+03, 2.02000e+03, 1.56400e+03,
       2.11900e+03, 2.62700e+03, 2.17700e+03, 2.49900e+03, 2.23000e+03,
       1.82500e+03, 1.43100e+03, 1.52100e+03, 2.08400e+03, 2.55100e+03,
       2.56900e+03, 2.32500e+03, 1.98100e+03, 1.60800e+03, 2.30700e+03,
       2.80800e+03, 2.32800e+03, 2.33400e+03, 2.18200e+03, 1.93600e+03,
       1.62600e+03, 1.92200e+03, 2.85800e+03, 2.81200e+03, 2.81200e+03,
       2.51700e+03, 2.36500e+03, 2.00000e+03, 2.32600e+03, 3.36800e+03,
       3.42700e+03, 3.92100e+03, 3.74700e+03, 3.58900e+03, 3.00000e+03,
       3.16400e+03, 3.89700e+03, 5.43100e+03, 6.16800e+03, 6.25600e+03,
       5.86000e+03, 4.73100e+03, 5.53300e+03, 7.94500e+03, 7.89600e+03,
       8.21000e+03, 8.04200e+03, 7.61900e+03, 6.28400e+03, 7.13500e+03,
       1.03620e+04, 1.07960e+04, 1.10520e+04, 1.11060e+04, 1.03200e+04,
       8.44600e+03, 1.00880e+04, 1.63070e+04, 1.74030e+04, 1.83500e+04,
       1.87120e+04, 1.81690e+04, 1.63010e+04, 1.85020e+04, 2.84180e+04,
       2.81990e+04, 2.89230e+04, 2.87940e+04, 2.63400e+04, 2.40100e+04,
       2.51700e+04, 3.49190e+04, 3.60600e+04, 3.85970e+04, 3.40160e+04,
       3.28030e+04, 2.83790e+04, 3.05030e+04, 4.45120e+04, 4.77060e+04,
       5.49090e+04, 6.20000e+04, 5.52630e+04, 3.84750e+04, 3.61810e+04,
       4.79240e+04, 3.98770e+04, 3.55480e+04, 3.12780e+04, 2.78170e+04,
       2.28520e+04, 2.21870e+04, 2.99800e+04, 2.95810e+04, 3.02370e+04,
       2.84320e+04, 2.47490e+04, 2.05690e+04, 2.09850e+04, 2.98400e+04,
       3.04720e+04, 3.23380e+04, 3.16590e+04, 2.80360e+04, 2.25400e+04,
       2.28870e+04, 3.21620e+04, 3.15180e+04, 3.33490e+04, 3.17260e+04,
       2.89730e+04, 2.50570e+04, 2.53260e+04, 3.69060e+04, 3.79190e+04,
       3.87390e+04, 3.65000e+04, 3.22310e+04, 2.85330e+04, 2.87430e+04,
       3.97150e+04, 3.76820e+04, 3.87770e+04, 3.76130e+04, 3.37430e+04,
       2.75990e+04, 2.61350e+04, 3.47730e+04, 4.52120e+04, 4.35320e+04,
       4.23290e+04, 3.86300e+04, 3.18100e+04, 3.18030e+04, 4.49290e+04,
       3.86190e+04, 3.58490e+04, 3.39740e+04, 2.91870e+04, 2.35330e+04,
       2.40600e+04, 3.46580e+04, 3.14340e+04, 3.04140e+04, 2.97090e+04,
       2.94790e+04, 2.66450e+04, 3.10840e+04, 4.07680e+04, 3.88480e+04,
       3.67570e+04, 3.58510e+04, 3.21090e+04, 2.85670e+04, 3.20830e+04,
       4.15890e+04, 3.65470e+04, 3.48360e+04, 3.26050e+04, 2.90580e+04,
       2.63160e+04, 3.20580e+04, 4.37340e+04, 3.92780e+04, 3.92640e+04,
       3.84650e+04, 3.56110e+04, 3.23060e+04, 3.64180e+04, 5.03040e+04,
       4.83210e+04, 4.77730e+04, 4.64200e+04, 4.35600e+04, 3.78780e+04,
       4.37530e+04, 5.77430e+04, 5.25290e+04, 5.16610e+04, 4.51930e+04,
       4.06650e+04, 3.51030e+04, 3.57650e+04, 4.74650e+04, 4.21240e+04,
       4.30450e+04, 4.13910e+04, 4.02510e+04, 3.35690e+04, 3.48140e+04,
       4.51090e+04, 3.80190e+04, 3.59860e+04, 3.36610e+04, 3.03180e+04,
       2.74360e+04, 3.05860e+04, 4.41280e+04, 4.22460e+04, 4.29420e+04,
       4.09990e+04, 3.77650e+04, 3.28830e+04, 3.55300e+04, 5.09490e+04,
       4.64290e+04, 4.58940e+04, 4.40610e+04, 3.96080e+04, 3.53350e+04,
       3.72520e+04, 5.07330e+04, 4.81970e+04, 4.67710e+04, 4.34240e+04,
       3.93290e+04, 3.33000e+04, 3.97040e+04, 5.62900e+04, 5.56940e+04,
       5.48190e+04, 5.03200e+04, 4.56670e+04, 3.87820e+04, 4.10510e+04,
       5.96920e+04, 5.62520e+04, 5.88250e+04, 5.69940e+04, 5.24910e+04,
       4.85940e+04, 5.31570e+04, 8.71700e+04, 1.02786e+05, 1.12699e+05,
       1.06048e+05, 9.58790e+04, 8.88830e+04, 8.91290e+04, 1.33966e+05,
       1.50292e+05, 1.61561e+05, 1.60634e+05, 1.37268e+05, 7.03620e+04,
       1.16275e+05, 1.95007e+05, 2.12463e+05, 2.72790e+05, 2.36573e+05,
       1.88564e+05, 1.18269e+05, 1.81065e+05, 2.29896e+05, 2.75647e+05,
       2.22170e+05, 1.72980e+05, 1.20288e+05, 9.36120e+04, 9.57880e+04,
       1.32955e+05, 1.15244e+05, 1.03221e+05, 9.64120e+04, 8.63250e+04,
       7.79480e+04, 9.80940e+04, 1.31514e+05, 1.18857e+05, 1.11758e+05,
       1.00325e+05, 9.17300e+04, 8.17330e+04, 1.02364e+05, 1.27364e+05,
       1.13201e+05, 1.08668e+05, 9.62020e+04, 8.40260e+04, 7.35050e+04,
       8.76980e+04, 1.05047e+05, 9.39490e+04, 8.84170e+04, 7.66420e+04,
       6.32640e+04, 5.23040e+04, 6.05470e+04, 7.64830e+04, 6.96610e+04,
       6.43390e+04, 5.22920e+04, 4.45570e+04, 3.75270e+04, 4.17550e+04,
       5.47460e+04, 5.25010e+04, 5.15700e+04, 4.47160e+04, 3.32390e+04,
       3.46480e+04, 3.77170e+04, 4.51270e+04, 3.91860e+04, 3.64760e+04,
       3.06310e+04, 2.78330e+04, 2.50860e+04, 3.13600e+04, 4.46410e+04,
       4.47880e+04, 4.61740e+04, 4.37610e+04, 4.14070e+04, 3.87530e+04,
       4.90230e+04, 6.85210e+04, 7.01070e+04, 7.35290e+04, 7.05030e+04,
       6.70290e+04, 6.20680e+04, 7.57290e+04, 9.98330e+04, 9.37030e+04,
       9.17540e+04, 8.28490e+04, 7.52830e+04, 6.74120e+04, 8.10490e+04,
       1.09281e+05, 9.90940e+04, 9.41760e+04, 8.28970e+04, 7.24300e+04,
       6.14510e+04, 6.83350e+04, 9.28520e+04, 8.01270e+04, 7.36400e+04,
       5.47820e+04, 4.74620e+04, 3.75840e+04, 4.21700e+04, 5.37160e+04,
       4.91010e+04, 4.47440e+04, 3.87060e+04, 3.29810e+04, 2.78810e+04,
       3.09470e+04, 3.73690e+04, 3.37690e+04, 3.16810e+04, 2.66380e+04,
       2.16100e+04, 1.99180e+04, 2.01420e+04, 2.52150e+04, 2.57660e+04,
       2.14440e+04, 1.84610e+04, 1.56960e+04, 1.32060e+04, 1.47130e+04,
       1.70990e+04, 1.45570e+04, 1.30490e+04, 1.15990e+04, 1.00070e+04,
       8.35400e+03, 9.03200e+03, 1.18910e+04, 1.33100e+04, 1.16640e+04,
       1.02110e+04, 8.94300e+03, 7.51600e+03, 9.06200e+03, 1.06940e+04,
       9.74300e+03, 8.72200e+03, 7.63800e+03, 6.93700e+03, 6.11800e+03,
       7.97300e+03, 9.41700e+03, 8.28400e+03, 7.63600e+03, 6.81800e+03,
       5.81700e+03, 5.01800e+03, 5.99700e+03, 7.31200e+03, 6.67900e+03,
       6.29100e+03, 5.75100e+03, 5.40600e+03, 4.98800e+03, 5.67800e+03,
       7.11400e+03, 7.09100e+03, 7.01300e+03, 6.20900e+03, 6.63700e+03,
       7.49000e+03, 9.81500e+03, 1.17450e+04, 1.14040e+04, 1.17840e+04,
       1.13140e+04, 1.07850e+04, 1.00740e+04, 1.26910e+04, 1.52730e+04,
       1.51380e+04, 1.48340e+04, 1.42200e+04, 1.39190e+04, 1.36250e+04,
       1.69930e+04, 1.99420e+04, 2.08940e+04, 2.08660e+04, 1.95870e+04,
       1.83430e+04, 1.67930e+04, 2.07730e+04, 2.50990e+04, 2.50370e+04,
       2.45990e+04, 2.42310e+04, 2.36390e+04, 2.19610e+04, 2.77760e+04,
       3.36980e+04, 3.14100e+04, 2.96810e+04, 2.64530e+04, 2.46060e+04,
       2.12430e+04, 2.50860e+04, 2.98240e+04, 2.69400e+04, 2.38550e+04,
       2.10980e+04, 1.83580e+04, 1.50120e+04, 1.72330e+04, 1.87130e+04,
       1.66660e+04, 1.61680e+04, 1.41540e+04, 1.23740e+04, 9.92700e+03,
       1.12710e+04, 1.32950e+04, 1.17180e+04, 1.05360e+04, 9.32400e+03,
       8.50300e+03, 7.32300e+03, 8.41900e+03, 9.82900e+03, 9.16300e+03,
       8.34100e+03, 7.28700e+03, 6.54700e+03, 5.41800e+03, 6.54300e+03,
       8.05500e+03, 7.30600e+03, 6.72700e+03, 6.18200e+03, 5.33000e+03,
       4.48300e+03, 5.35900e+03, 6.40700e+03, 5.53900e+03, 4.98600e+03,
       4.43200e+03, 3.82900e+03, 3.26800e+03, 4.06800e+03, 5.14800e+03,
       4.71500e+03, 4.52600e+03, 3.77400e+03, 3.43400e+03, 3.08400e+03,
       3.42900e+03, 4.64700e+03, 5.18700e+03, 4.56800e+03, 4.23000e+03,
       3.65600e+03, 3.31500e+03, 4.17100e+03, 4.15200e+03, 3.45000e+03,
       2.09300e+03]

days = len(covid_data_uk)

import matplotlib.pyplot as plt
plt.figure(figsize=(7,4))