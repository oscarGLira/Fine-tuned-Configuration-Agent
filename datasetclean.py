import pandas as pd

# Open dataset
dataset_name = 'requirements.csv'

# Read the dataset into a DataFrame
df = pd.read_csv(dataset_name)

# List of phrases to check for
none_phrases = [
    "None mentioned in the provided text.",
    "None explicitly stated. The text appears to be a disclaimer or a liability waiver, rather than a statement of requirements.",
    "None mentioned in this text.",
    "None mentioned in the given text.",
    "None specified in this text.",
    "None explicitly mentioned in the text.",
    "None explicitly stated in this section of the guide.",
    "NaN",
    "**",
    "** None mentioned in the text.",
    "N/A (Not provided in the text)",
    "Not provided in the given text.",
    "None mentioned. The text does not discuss specific device configurations, settings, or parameters. It is primarily focused on disclaiming warranties and liabilities related to the software or manual being described.",
    "** None mentioned in this text. The text does not contain any technical or device-related configurations.",
    "Requirement: None specified in this text. The text appears to be a general information page with links to various resources.  Configuration: IP Addressing: ARP Configuration Guide, Cisco IOS XE Gibraltar 16.11.x",
    "Requirement: ARP (Address Resolution Protocol) finds the hardware address (Media Access Control or MAC address) of a host from its known IP address.  Configuration:  * Static ARP entries * Timeout for dynamic ARP entries * Clearing the cache * Proxy ARP",
    "None explicitly mentioned in the text. However, the text does mention Cisco Feature Navigator as a resource for finding information about platform support and software image support.",
    "ARP Configuration Guide (Cisco IOS XE Gibraltar 16.11.x)",
    "None specified in this text, but it mentions that for supported interface types, refer to the data sheet for your hardware platform.",
    "Cisco IOS XE Gibraltar 16.11.x"
]

# Function to check if any none phrases are contained within the text
def contains_none_phrases(text):
    if isinstance(text, str):
        return any(phrase in text for phrase in none_phrases)
    return False

# Filter out rows where either column is empty or contains any of the none phrases
df_cleaned = df.dropna(subset=['requirement', 'configuration'])
df_cleaned = df_cleaned[~df_cleaned['requirement'].apply(contains_none_phrases) & ~df_cleaned['configuration'].apply(contains_none_phrases)]

# Save the cleaned data to a new CSV file
cleaned_dataset_name = 'requirements_cleaned.csv'
df_cleaned.to_csv(cleaned_dataset_name, index=False)

# Show the cleaned DataFrame
print(df_cleaned)
print(f"Cleaned dataset saved as '{cleaned_dataset_name}'.")
