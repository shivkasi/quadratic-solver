import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', message='urllib3 v2 only supports')

import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define the date range (last 5 years)
end_date = datetime.now()
start_date = end_date - timedelta(days=5*365)

# Download NVDA data
print("Downloading NVDA data...")
nvda = yf.download('NVDA', start=start_date, end=end_date)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(nvda.index, nvda['Close'], linewidth=2, color='#76B900')
plt.title('NVIDIA (NVDA) Stock Price - Last 5 Years', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the plot
plt.savefig('nvda_plot.png', dpi=300, bbox_inches='tight')
print("Plot saved as 'nvda_plot.png'")

# Display the plot
plt.show()
