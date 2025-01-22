import pandas as pd
import hashlib
import logging

class DataPrivacy:
    def __init__(self, salt="random_salt"):
        self.salt = salt
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    def _hash_value(self, value):
        """
        Hash a single value with salt for anonymization.
        """
        salted_value = f"{value}{self.salt}"
        hashed_value = hashlib.sha256(salted_value.encode()).hexdigest()
        return hashed_value

    def anonymize_data(self, df, sensitive_columns):
        """
        Anonymize multiple sensitive columns.
        
        Args:
            df (pd.DataFrame): Input DataFrame.
            sensitive_columns (list): Columns to anonymize.

        Returns:
            pd.DataFrame: Anonymized DataFrame.
        """
        anonymized_df = df.copy()
        for column in sensitive_columns:
            logging.info(f"Anonymizing column: {column}")
            anonymized_df[column] = anonymized_df[column].apply(self._hash_value)
        return anonymized_df

    def mask_data(self, df, mask_columns):
        """
        Mask sensitive data partially for usability.
        """
        masked_df = df.copy()
        for column in mask_columns:
            logging.info(f"Masking column: {column}")
            masked_df[column] = masked_df[column].apply(lambda x: f"{x[:3]}***" if isinstance(x, str) else x)
        return masked_df

# Example usage
if __name__ == "__main__":
    sample_data = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Email": ["alice@example.com", "bob@example.com", "charlie@example.com"],
        "Age": [25, 30, 35]
    })
    privacy_agent = AdvancedDataPrivacy(salt="secure_salt")
    anonymized = privacy_agent.anonymize_data(sample_data, ["Name", "Email"])
    masked = privacy_agent.mask_data(sample_data, ["Email"])
    print("Anonymized Data:\n", anonymized)
    print("Masked Data:\n", masked)