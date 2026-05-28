# References — canonical theory papers

20 papers, mostly Econometrica, all heavily theoretical, published 2010–2022. These are **study material** for the Phase 0 analysis pass that produced [STRUCTURE.md](../STRUCTURE.md) — not runtime references for the writing roles.

If you need to understand a structural convention more deeply than STRUCTURE.md captures, read the relevant papers here. Otherwise the spec is enough.

## Where the PDFs live

PDFs live **outside the repo**, at:

```
/Users/p-aldighieri/Library/CloudStorage/OneDrive-Personal/Economia/Projetos/Ai4Science/theory_paper_samples
```

Inside the repo, `references/pdfs/` is a **symlink** to that directory (gitignored — the symlink is per-machine).

### One-time setup on a new machine

```bash
ln -s "/Users/p-aldighieri/Library/CloudStorage/OneDrive-Personal/Economia/Projetos/Ai4Science/theory_paper_samples" references/pdfs
```

## The list

| # | Authors | Year | Title | Journal | DOI | Subfield |
|---|---|---|---|---|---|---|
| 1 | Kamenica, Gentzkow | 2011 | Bayesian Persuasion | AER 101(6) | [10.1257/aer.101.6.2590](https://doi.org/10.1257/aer.101.6.2590) | Info design |
| 2 | Ortoleva | 2012 | Modeling the Change of Paradigm: Non-Bayesian Reactions to Unexpected News | AER 102(6) | [10.1257/aer.102.6.2410](https://doi.org/10.1257/aer.102.6.2410) | Decision theory |
| 3 | Bergemann, Morris | 2013 | Robust Predictions in Games with Incomplete Information | Econometrica 81(4) | [10.3982/ECTA11105](https://doi.org/10.3982/ECTA11105) | Robust info design |
| 4 | Pavan, Segal, Toikka | 2014 | Dynamic Mechanism Design: A Myersonian Approach | Econometrica 82(2) | [10.3982/ECTA10269](https://doi.org/10.3982/ECTA10269) | Dynamic mech design |
| 5 | Halac, Yared | 2014 | Fiscal Rules and Discretion Under Persistent Shocks | Econometrica 82(5) | [10.3982/ECTA11207](https://doi.org/10.3982/ECTA11207) | Dynamic contracts |
| 6 | Ely, Frankel, Kamenica | 2015 | Suspense and Surprise | JPE 123(1) | [10.1086/677350](https://doi.org/10.1086/677350) | Dynamic info design |
| 7 | Carroll | 2015 | Robustness and Linear Contracts | AER 105(2) | [10.1257/aer.20131159](https://doi.org/10.1257/aer.20131159) | Robust contracts |
| 8 | Hart, Reny | 2015 | Maximal Revenue with Multiple Goods | TE 10(3) | [10.3982/TE1517](https://doi.org/10.3982/TE1517) | Multi-good mech design |
| 9 | Fudenberg, Iijima, Strzalecki | 2015 | Stochastic Choice and Revealed Perturbed Utility | Econometrica 83(6) | [10.3982/ECTA12660](https://doi.org/10.3982/ECTA12660) | Decision theory |
| 10 | Cerreia-Vioglio, Dillenberger, Ortoleva | 2015 | Cautious Expected Utility and the Certainty Effect | Econometrica 83(2) | [10.3982/ECTA11733](https://doi.org/10.3982/ECTA11733) | Decision theory |
| 11 | Bergemann, Brooks, Morris | 2015 | The Limits of Price Discrimination | AER 105(3) | [10.1257/aer.20130848](https://doi.org/10.1257/aer.20130848) | Info design |
| 12 | Bergemann, Morris | 2016 | Bayes Correlated Equilibrium and the Comparison of Information Structures in Games | TE 11(2) | [10.3982/TE1808](https://doi.org/10.3982/TE1808) | Info design |
| 13 | Hörner, Skrzypacz | 2016 | Selling Information | JPE 124(6) | [10.1086/688874](https://doi.org/10.1086/688874) | Info / dynamic games |
| 14 | Roesler, Szentes | 2017 | Buyer-Optimal Learning and Monopoly Pricing | AER 107(7) | [10.1257/aer.20160145](https://doi.org/10.1257/aer.20160145) | Info design |
| 15 | Carroll | 2017 | Robustness and Separation in Multidimensional Screening | Econometrica 85(2) | [10.3982/ECTA14165](https://doi.org/10.3982/ECTA14165) | Robust mech design |
| 16 | Kolotilin, Mylovanov, Zapechelnyuk, Li | 2017 | Persuasion of a Privately Informed Receiver | Econometrica 85(6) | [10.3982/ECTA13251](https://doi.org/10.3982/ECTA13251) | Persuasion |
| 17 | Daskalakis, Deckelbaum, Tzamos | 2017 | Strong Duality for a Multiple-Good Monopolist | Econometrica 85(3) | [10.3982/ECTA12618](https://doi.org/10.3982/ECTA12618) | Multi-good mech design |
| 18 | Akbarpour, Li | 2020 | Credible Auctions: A Trilemma | Econometrica 88(2) | [10.3982/ECTA15925](https://doi.org/10.3982/ECTA15925) | Mech design |
| 19 | Lipnowski, Ravid | 2020 | Cheap Talk with Transparent Motives | Econometrica 88(4) | [10.3982/ECTA15674](https://doi.org/10.3982/ECTA15674) | Cheap talk |
| 20 | Doval, Skreta | 2022 | Mechanism Design with Limited Commitment | Econometrica 90(4) | [10.3982/ECTA16846](https://doi.org/10.3982/ECTA16846) | Mech design |

## Download notes

For future additions, the Northwestern proxy URLs that worked for batch download:

- **Wiley** (Econometrica, TE): `https://onlinelibrary-wiley-com.turing.library.northwestern.edu/doi/pdfdirect/<DOI>?download=true`
- **AEA** (AER): `https://pubs-aeaweb-org.turing.library.northwestern.edu/doi/pdf/<DOI>?download=true`
- **U Chicago** (JPE): `https://www-journals-uchicago-edu.turing.library.northwestern.edu/doi/pdf/<DOI>?download=true`

Direct navigation triggers a download (no PDF-reader detour). Each takes ~8 seconds.
