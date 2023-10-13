import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Define the gradient background for the title
title_background = """
linear-gradient(-245deg,#8a2387,#e94057,#f27121,gold);
"""

# Use HTML and CSS to style the title
title_html = f"""
    <div style="background: {title_background}; padding: 20px; border-radius: 10px;">
        <h1 style="color: black; text-align: center; font-size: 36px;">Trip Places Suggestor—DestiDive🌅</h1>
    </div>
"""

# Display the styled title using markdown
st.markdown(title_html, unsafe_allow_html=True)

custom_css = """
<style>
[data-testid="stAppViewContainer"]
{
  background-image: linear-gradient(-310deg,cyan,black,maroon,blue,brown,yellow ,red);
}
[data-testid="stHeader"]
{
 position: fixed;
    top: 0px;
    left: 0px;
    right: 0px;
    height: 2.875rem;
    background: linear-gradient(245deg,#8a2387,#e94057,#f27121);
    outline: none;
    z-index: 999990;
    display: block;
    transition: all 0.3s ease-in-out;
}

[data-testid="stImage"] {
    border: 25px double transparent;
    border-radius: 20px;
    transition: all 0.3s ease-in-out;
    box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
}

[data-testid="stImage"]:hover {
    transform: scale(1.05);
    #filter: grayscale(100%);
     #filter: sepia(100%);
     filter: hue-rotate(90deg);
}

[data-testid="stSidebar"]
{
 background: linear-gradient(270deg,purple,violet,maroon);
  background: linear-gradient(245deg,#8a2387,#e94057,#f27121);
}
body {
    background: linear-gradient(45deg, gold, blue, yellow, pink);
}
.sidebar.stTextInput {
    text-align: center;
    border-radius: 50px;
    border: 2px solid #fff;
}
.highlight-service:hover {
 transform: scale(1.05);
     background: radial-gradient(circle,green,white,orange);
    /* Add other styles like text color, padding, etc. */
    color: #333; /* Text color for contrast */
    padding: 7px; /* Adjust padding as needed */
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Load the updated dataset (replace 'preparedataupd.csv' with the actual file path)
data = pd.read_csv(r"destidata.csv")

# Drop rows with null values
data = data.dropna(how='any')

# Encode categorical features like DESTINATION and CATEGORY
label_encoder_destination = LabelEncoder()
data['DESTINATION_ENCODED'] = label_encoder_destination.fit_transform(
    data['DESTINATION'].str.strip())  # Strip whitespace

label_encoder_service = LabelEncoder()
data['SERVICE_NAME_ENCODED'] = label_encoder_service.fit_transform(
    data['SERVICE_NAME'].str.strip())  # Strip whitespace

# One-hot encode the 'CATEGORY' feature
category_encoder = OneHotEncoder()
category_encoded = category_encoder.fit_transform(data[['CATEGORY']]).toarray()
category_columns = category_encoder.get_feature_names_out(['CATEGORY'])
data[category_columns] = pd.DataFrame(
    category_encoded, columns=category_columns)

# Load the trained KNN model
with open("knn_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Add a logo to the top of the app
st.image('logo.png', use_column_width=True)

# Input form
st.sidebar.header('Destiantion As Input ')

# Create select box for user input
destination_names = [
    "Mumbai, Maharashtra, India",
    "Goa, India",
    "Mussoorie, Uttarakhand, India",
    "Mcleodganj, Himachal Pradesh, India",
    "Chennai, Tamil Nadu, India",
    "Dubai - United Arab Emirates",
    "Mysore, Karnataka, India",
    "Mauritius",
    "Chikmagalur, Karnataka, India",
    "Shimla, Himachal Pradesh, India",
    "Udupi, Karnataka, India",
    "Dharamshala, Himachal Pradesh, India",
    "Jaipur, Rajasthan, India",
    "Hyderabad, Telangana, India",
    "Ooty - Masinagudi - Mudumalai, Tamil Nadu, India",
    "Udaipur, Rajasthan, India",
    "Andaman and Nicobar Islands, India",
    "Madikeri - Coorg, Karnataka, India",
    "Jaisalmer, Rajasthan, India",
    "Malé, Maldives",
    "Alleppey, Kerala, India",
    "Pune, Maharashtra, India",
    "Lansdowne, Uttarakhand, India",
    "Alappuzha, Kerala, India",
    "Gulmarg, Jammu & Kashmir, India",
    "Shirdi, Maharashtra, India",
    "Rameswaram, Tamil Nadu, India",
    "Munnar, Kerala, India",
    "Kolkata, West Bengal, India",
    "Agra, Uttar Pradesh, India",
    "Manali, Himachal Pradesh, India",
    "Nainital, Uttarakhand, India",
    "Pondicherry, India",
    "Shillong, Meghalaya, India",
    "Auckland, New Zealand",
    "Hampi, Karnataka, India",
    "Mahabalipuram, Tamil Nadu, India",
    "Darjeeling, West Bengal, India",
    "Madikeri, Karnataka, India",
    "Thekkady, Kerala, India",
    "Dalhousie, Himachal Pradesh, India",
    "Picton, New Zealand",
    "Gokarna - Udupi - Mangalore, Karnataka, India",
    "Varanasi, Uttar Pradesh, India",
    "Franz Josef, New Zealand",
    "Delhi - Noida - NCR, India",
    "Nelson, New Zealand",
    "Ahmedabad, Gujarat, India",
    "Wellington, New Zealand",
    "Corbett, Uttarakhand, India",
    "Kovalam, Kerala, India",
    "Agumbe - Shimoga, Karnataka, India",
    "Delhi, India",
    "Palampur, Himachal Pradesh, India",
    "Pushkar, Rajasthan, India",
    "Coromandel, New Zealand",
    "Almora, Uttarakhand, India",
    "Ajmer, Rajasthan, India",
    "Kochi, Kerala, India",
    "Tirupati, Andhra Pradesh, India",
    "Amarnath - Pahalgam, Jammu & Kashmir, India",
    "Dehradun, Uttarakhand, India",
    "Rishikesh, Uttarakhand, India",
    "New Plymouth, New Zealand",
    "Kodaikanal, Tamil Nadu, India",
    "Rajkot, Gujarat, India",
    "Gir National Park, Gujarat",
    "Bikaner, Rajasthan, India",
    "Binsar, Uttarakhand, India",
    "Haridwar, Uttarakhand, India",
    "Amritsar, Punjab, India",
    "Jodhpur, Rajasthan, India",
    "Kasol, Himachal Pradesh, India",
    "Kanyakumari, Tamil Nadu, India",
    "Mathura, Uttar Pradesh, India",
    "Napier, New Zealand",
    "Cherrapunji, Meghalaya, India",
    "Abu Dhabi - United Arab Emirates",
    "Mukteshwar, Uttarakhand, India",
    "Mahabaleshwar, Maharashtra, India",
    "Kohima, Nagaland, India",
    "Taupo, New Zealand",
    "Gokarna, Karnataka, India",
    "Kullu, Himachal Pradesh, India",
    "Lonavla, Maharashtra, India",
    "Visakhapatnam, Andhra Pradesh, India",
    "Gangtok, Sikkim, India",
    "Yercaud, Tamil Nadu, India",
    "Kaikoura, New Zealand",
    "Madurai, Tamil Nadu, India",
    "Puri, Odisha, India",
    "Srinagar, India",
    "Kaziranga, Assam, India",
    "Katra, Jammu & Kashmir, India",
    "Colombo, Sri Lanka",
    "Kanatal, Kaudia Range, Uttarakhand, India",
    "Varkala, Kerala, India",
    "Mount Abu, Rajasthan, India",
    "Ramnagar, Uttarakhand, India",
    "Thiruvananthapuram, Kerala, India",
    "Kausani, Uttarakhand, India",
    "Gujarat, India",
    "Queenstown, New Zealand",
    "Dunedin, New Zealand",
    "Poovar, Kerala, India",
    "Panchgani, Maharashtra, India",
    "Ranikhet, Uttarakhand, India",
    "Khajuraho, Madhya Pradesh, India",
    "Ooty, Tamil Nadu, India",
    "Leh",
    "Lachen, Sikkim, India",
    "Sharjah - United Arab Emirates",
    "Bay Of Islands, New Zealand",
    "Rotorua, New Zealand",
    "Hamilton, New Zealand",
    "Leh - Ladakh",
    "Coorg, Karnataka, India",
    "Kathmandu, Nepal",
    "Gisborne, New Zealand",
    "Invercargill, New Zealand",
    "Agumbe, Karnataka, India",
    "Wayanad, Kerala, India",
    "Kuala Lumpur, Malaysia",
    "Kurnool, Andhra Pradesh, India",
    "Leh - Ladakh, India",
    "Lake Tekapo, New Zealand",
    "Paro, Bhutan",
]

# Select destination using a select box
destination = st.sidebar.selectbox('Select Destination', destination_names)

# Center-align and style the input box
st.sidebar.markdown(
    f'<div class="stTextInput highlight-service">{destination}</div>',
    unsafe_allow_html=True
)

# Make predictions when the 'Predict' button is clicked
if st.sidebar.button('LETS GO🏌🏼!'):
    # Encode the destination input
    encoded_destination = label_encoder_destination.transform([destination])[0]

    # Filter the data for the specified DESTINATION
    filtered_data = data[data['DESTINATION_ENCODED']
                         == encoded_destination].copy()
    filtered_data['PREDICTED_CHECK_VALUE'] = model.predict(
        filtered_data[['DESTINATION_ENCODED', 'SERVICE_NAME_ENCODED', 'RATING', 'WEIGHTAGE', 'COUNT'] + list(category_columns)])

    # Keep track of printed services
    printed_services = set()

    # Display the services and their respective check values with hover effect
    st.subheader(
        f'Services in {destination} (Ordered by Priority considering important facotrs 😀)')
    for index, row in filtered_data[filtered_data['PREDICTED_CHECK_VALUE'] > 0].sort_values(by='PREDICTED_CHECK_VALUE', ascending=False).iterrows():
        service_name = row['SERVICE_NAME']

        # Skip printing "futureservicedummy"
        if service_name == "futureservicedummy":
            continue

        if service_name not in printed_services:
            st.markdown(
                f'<div class="highlight-service">Service: {service_name}</div>'
                f'<div class="highlight-service">Category: {row["CATEGORY"]}</div>'
                # f'<div class="highlight-service">Predicted Check Value: {row["PREDICTED_CHECK_VALUE"]:.2f}</div>'
                '<hr class="highlight-service">',
                unsafe_allow_html=True
            )
            printed_services.add(service_name)

    if not printed_services:
        st.subheader(
            f'No services found with non-zero check value for {destination}')
