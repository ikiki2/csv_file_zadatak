import pandas as pd

carrier_plans_data = pd.read_csv("carrier-plans.csv")
resale_plans_data = pd.read_csv("resale-plans.csv")

#Merge datasets by 'mdn' 
merged_plans_data = pd.merge(carrier_plans_data, resale_plans_data, on='mdn')
#merged_plans_data = pd.merge(carrier_plans_data, resale_plans_data, left_on='mdn', right_on='mdn')
merged_data_frame = pd.DataFrame(merged_plans_data)
merged_data_frame = merged_data_frame[['mdn', 'customer', 'sprint_plan', 'resale_plan', 'socs']]
merged_data_frame.to_csv('plans_data.csv', index=None)

#Create LTE SOC value data
lte_soc_data_frame = merged_data_frame[['mdn', 'customer', 'sprint_plan', 'resale_plan']].copy()
lte_soc_data_frame["lte_socs"] = ['Y' if 'DSMLTESOC' in x else 'N' for x in merged_data_frame['socs']]
lte_soc_data_frame.to_csv('lte_soc_plans_data.csv', index=None)

#Give device ammount
device_dict = {}
for device in merged_data_frame['resale_plan']:
    device_dict[device] = device_dict.get(device, 0) + 1

dev_ammount_data_frame = pd.DataFrame({'resale_plan':[], 'num_of_devices':[]})
dev_ammount_data_frame["resale_plan"] = [key for key in device_dict.keys()]
dev_ammount_data_frame["num_of_devices"] = [num for num in device_dict.values()]
dev_ammount_data_frame.to_csv('dev_amm_plans_data.csv', index=None)







