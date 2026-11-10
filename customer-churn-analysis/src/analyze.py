from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / 'data' / 'customers.csv')
summary = df.groupby('contract_type').agg(customers=('customer_id','count'), churn_rate=('churn','mean'), average_monthly_charge=('monthly_charge','mean')).reset_index()
summary['churn_rate'] = (summary['churn_rate']*100).round(2)
summary.to_csv(ROOT/'outputs'/'contract_summary.csv',index=False)
print('Customers:',len(df));print('Churn rate: {:.2%}'.format(df.churn.mean()));print(summary.to_string(index=False))
fig, ax=plt.subplots(figsize=(8,5));ax.bar(summary.contract_type,summary.churn_rate);ax.set(ylabel='Churn rate (%)',title='Customer churn by contract type');fig.tight_layout();fig.savefig(ROOT/'outputs'/'churn_by_contract.png',dpi=160);plt.close(fig)
