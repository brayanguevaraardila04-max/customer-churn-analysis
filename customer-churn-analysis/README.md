# Customer Churn Analysis | Python Data Analytics

**Portfolio case study using synthetic telecom customer data.** This is an independent simulated business scenario, not client work or actual company records.

## Business question
Which customer segments show the highest churn, and how might a telecom business prioritize retention initiatives?

## Tools
Python, Pandas, Matplotlib, CSV.

## Data
`data/customers.csv` contains 2,000 **synthetically generated** customer records. Fields: `customer_id`, `contract_type`, `tenure_months`, `monthly_charge`, `support_tickets`, `internet_service`, `churn` (1 = churned). This dataset is artificial and associations do not prove causation.

## Run
```bash
pip install -r requirements.txt
python src/analyze.py
```

## Deliverables
- `src/analyze.py`: reproducible analysis
- `outputs/contract_summary.csv`: contract-level churn comparison
- `outputs/churn_by_contract.png`: visualization
- `docs/findings.md`: summary and limitations

## Analytical workflow
1. Validate fields and missing values.
2. Calculate overall churn and segment churn rates.
3. Compare churn by contract type and monthly charges.
4. Interpret descriptive associations and suggest follow-up tests.

## Limitations
All data are synthetic. No causal inference or real-world business outcomes are claimed.
