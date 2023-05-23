#from functions import *
import datetime
import warnings
warnings.filterwarnings("ignore")
import os
import plotly.express as px
##import functions
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.0f' % x)

df = pd.read_excel("C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/hotel_info.xlsx")
hotel = pd.read_excel("C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/hotel_info.xlsx", sheet_name="hotel")
ratings = pd.read_excel("C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/hotel_info.xlsx", sheet_name="ratings")
df_ = pd.merge(hotel, ratings, how="left", on=["hotel_id"])
df = df_.copy()
df.head()

#GENEL SAYFA AYARI
st.set_page_config(
    page_title=" MYADVICE - BOOKING HOTELS IN LUDWIGSBURG",
    page_icon="⬛",
    layout="wide",
    initial_sidebar_state="auto"
)

tabs = ["Page_1"]

#SIDEBAR MYADVICE LOGOSU EKLEME
from PIL import Image
image_path = "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/nese7.png"
image = Image.open(image_path)
st.sidebar.image(image, use_column_width=True)


#QUICK SEARCH YAZISI
#st.sidebar.markdown("<h1 style='text-align:center;'>QUICK SEARCH</h1>", unsafe_allow_html=True)
image_path = "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/quick_search_nese.jpg"
image = Image.open(image_path)
st.sidebar.image(image, use_column_width=True)

#CHECK-IN DATE, CHECK-OUT DATE, ADULT, CHILDREN VE ROOM SEÇİMİ
def main():
    # Yan çubukta check-in ve check-out tarih seçimi için takvimleri görüntüleme
    check_in_date = st.sidebar.date_input("CHECK-IN DATE", value=datetime.today())
    check_out_date = st.sidebar.date_input("CHECK-OUT DATE", value=datetime.today())

    # Check-in ve check-out tarihlerini kontrol etme
    if check_in_date < datetime.today().date():
        st.sidebar.warning("Geçerli bir check-in tarihi giriniz!")
    elif check_out_date < check_in_date:
        st.sidebar.warning("Geçerli bir check-out tarihi giriniz!")

    col1, col2, col3 = st.sidebar.columns([2, 2, 2])
    adult_input = col1.number_input("ADULT", step=1, min_value=0)
    children_input = col2.number_input("CHILDREN", step=1, min_value=0)
    room_input = col3.number_input("ROOM", step=1, min_value=0)

    # Arama butonunu ekleme
    col4, col5, col6 = st.sidebar.columns([3,3,3])
    search_button = col5.button("SEARCH")

    # Arama butonuna basıldığında işlemleri gerçekleştirme
    #if search_button:
        # Seçilen değerleri kullanarak arama işlemlerini yapabilirsiniz
    #st.sidebar.write("Arama işlemi gerçekleştirildi!")
    #st.sidebar.write("Check-in tarihi:", check_in_date)
    #st.sidebar.write("Check-out tarihi:", check_out_date)
    #st.sidebar.write("Yetişkin:", adult_input)
    #st.sidebar.write("Çocuk:", children_input)
    #st.sidebar.write("Oda:", room_input)

if __name__ == '__main__':
    main()




#DETAILED SEARCH YAZISI
#st.sidebar.markdown("<h1 style='text-align:center;'>DETAILED SEARCH</h1>", unsafe_allow_html=True)
image_path = "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/detailedsearch.png"
image = Image.open(image_path)
st.sidebar.image(image, use_column_width=True)

#BREAKFAST OPTIONS
st.sidebar.write("<h3>Breakfast Options</h3>", unsafe_allow_html=True)
col1, col2  = st.sidebar.columns([5,2])
no_breakfast = col1.checkbox("No Breakfast")
col1, col2  = st.sidebar.columns([5,2])
american_breakfast = col1.checkbox("American Breakfast")
col1, col2  = st.sidebar.columns([5,2])
continental_breakfast = col1.checkbox("Continental Breakfast")
col1, col2  = st.sidebar.columns([5,2])
vegeterian_breakfast = col1.checkbox("Vegeterian Breakfast")
col1, col2  = st.sidebar.columns([5,2])
glutenfree_breakfast = col1.checkbox("Gluten-Free Breakfast")
col1, col2  = st.sidebar.columns([5,2])
openbuffet_breakfast = col1.checkbox("Open-Buffet Breakfast")
col1, col2  = st.sidebar.columns([5,2])
takeaway_breakfast = col1.checkbox("Take-Away Breakfast")
st.sidebar.write("", unsafe_allow_html=True)


#BANNER FOTOSU EKLEME
from PIL import Image
#SLOGAN FOTOĞRAFI
def main():
    # Fotoğraf ekleme örneği
    image_path = "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/myadvice_nese.jpg"
    image = Image.open(image_path)
    #st.image(image, caption='Ludwigsburg', use_column_width=True)
    st.image(image, use_column_width=True)

if __name__ == '__main__':
    main()

#SAĞ KAPAK FOTOĞRAFI
def main():
    # Fotoğraf ekleme örneği
    image_path = "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/cover_photo_1.jpg"
    image = Image.open(image_path)
    #st.image(image, caption='Ludwigsburg', use_column_width=True)
    st.image(image, use_column_width=True)

    if __name__ == '__main__':
        main()

lake_view = True
city_view = True
hotel_type = True
guest_house_type = True
credit_card = True
payment_refund = True
restaurant = True
non_smoking = True
fitness = True
pet = True


########################################################################################
########################################################################################
########################################################################################
########################################################################################

# Başlangıçta tüm otelleri önerilen otellere atayın
recommended_hotels = df.copy()
st.subheader("ADVICED FEATURES")
# breakfast seçeneklerine göre filtreleme
if no_breakfast:
    recommended_hotels = recommended_hotels[recommended_hotels["breakfast"] == 0]
if american_breakfast:
    recommended_hotels = recommended_hotels[recommended_hotels["breakfast_american"] == 1]
if continental_breakfast:
    recommended_hotels = recommended_hotels[recommended_hotels["breakfast_continental"] == 1]
if vegeterian_breakfast:
    recommended_hotels = recommended_hotels[recommended_hotels["breakfast_vegetarian"] == 1]
if glutenfree_breakfast:
    recommended_hotels = recommended_hotels[recommended_hotels["breakfast_glutenfree"] == 1]
if openbuffet_breakfast:
    recommended_hotels = recommended_hotels[recommended_hotels["breakfast_openbuffet"] == 1]
if takeaway_breakfast:
    recommended_hotels = recommended_hotels[recommended_hotels["takeaway_breakfast"] == 1]

# Aynı otelleri kaldırın ve benzersiz otelleri getirin
recommended_hotels = recommended_hotels.drop_duplicates(subset=["hotel_name_x"])

# Ratinge göre sıralama ve ilk 5 oteli getirme
recommended_hotels = recommended_hotels.sort_values("reviews", ascending=False).head(5)





####################################################################
##################OTEL DETAYLARI FOTOLU#############################
####################################################################
# Tek bir otel önerisi yerine tüm önerilen otelleri gösterin

for index, hotel in recommended_hotels.iterrows():
    #st.write(hotel["hotel_name_x"])
    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])

    hotel_name = hotel['hotel_name_x'].upper()
    col1.markdown(f"<b>NAME:</b> {hotel_name}", unsafe_allow_html=True)
    # col1.markdown(f"<b>NAME:</b> {hotel['hotel_name_x']}", unsafe_allow_html=True)

    image_path = hotel['hotel_star_icon']
    if os.path.exists(image_path):
        image = Image.open(image_path)
        col2.image(image, use_column_width=False)
    col3.markdown(f'<a href="{hotel["embed"]}">Show on map</a>', unsafe_allow_html=True)
    st.markdown(f"<b>PRICE (per night/€):</b> {hotel['weekdays_price']}", unsafe_allow_html=True)
    #st.markdown(f"<b>STAR:</b> {hotel['hotel_star']}", unsafe_allow_html=True)
    st.markdown(f"<b>DESCRIPTION:</b> {hotel['hotel_description']}", unsafe_allow_html=True)

    image_path = hotel['hotel_image']
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption=hotel['hotel_name_x'], use_column_width=True)
    else:
        st.write("Görüntü bulunamadı.")
    st.write("---")
########################################################################################
########################################################################################
########################################################################################
########################################################################################















# Öneri yapma
st.subheader("ADVICED FEATURES")
for _, hotel in df.iterrows():
    col1, col2, col3, col4, col5 = st.columns([2,1,1,1,1])

    hotel_name = hotel['hotel_name_x'].upper()
    col1.markdown(f"<b>NAME:</b> {hotel_name}", unsafe_allow_html=True)
    #col1.markdown(f"<b>NAME:</b> {hotel['hotel_name_x']}", unsafe_allow_html=True)

    image_path = hotel['hotel_star_icon']
    if os.path.exists(image_path):
        image = Image.open(image_path)
        col2.image(image, use_column_width=False)
    col3.markdown(f'<a href="{hotel["embed"]}">Show on map</a>', unsafe_allow_html=True)



    # number_of_reviews değişkenini link olarak görüntüleyin

    #col4.markdown(f"{hotel['number_of_reviews']} reviews", unsafe_allow_html=True)
    #col4.markdown(f"<a href='#{hotel['reviews']}' target='_blank'>{hotel['number_of_reviews']} reviews</a>", unsafe_allow_html=True)

########################

    ########################
    st.markdown(f"<b>PRICE (per night/€):</b> {hotel['weekdays_price']}", unsafe_allow_html=True)
    #st.markdown(f"<b>STAR:</b> {hotel['hotel_star']}", unsafe_allow_html=True)
    st.markdown(f"<b>DESCRIPTION:</b> {hotel['hotel_description']}", unsafe_allow_html=True)

    image_path = hotel['hotel_image']
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption=hotel['hotel_name_x'], use_column_width=True)
    else:
        st.write("Görüntü bulunamadı.")
    st.write("---")





#FACILITIES
st.sidebar.write("<h3>Facilities</h3>", unsafe_allow_html=True)
col1, col2  = st.sidebar.columns([5,2])
restaurant = col1.checkbox("Restaurant")
col1, col2  = st.sidebar.columns([5,2])
bar = col1.checkbox("Bar")
col1, col2  = st.sidebar.columns([5,2])
non_smoking = col1.checkbox("Non-Smoking")
col1, col2  = st.sidebar.columns([5,2])
fitness = col1.checkbox("Fitness")
col1, col2  = st.sidebar.columns([5,2])
pet = col1.checkbox("Pet")
st.sidebar.write("", unsafe_allow_html=True)



#HOTEL TYPE
st.sidebar.write("<h3>Business Types</h3>", unsafe_allow_html=True)
###Çalışıyor; uygun icon jpg gerekli
#from PIL import Image
#col1, col2 = st.sidebar.columns([1, 2])
#col2.markdown("<h3>Business Types</h3>", unsafe_allow_html=True)
#image_path = "C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/down_arrow_transp_3_1.png"
#image = Image.open(image_path)
#col1.image(image, use_column_width=True)

col1, col2  = st.sidebar.columns([5,2])
hotel_type = col1.checkbox("Hotel")
col1, col2  = st.sidebar.columns([5,2])
guest_house_type = col1.checkbox("Guest House")
col1, col2  = st.sidebar.columns([5,2])
st.sidebar.write("", unsafe_allow_html=True)




#PAYMENT METHOD
st.sidebar.write("<h3>Payment</h3>", unsafe_allow_html=True)
col1, col2  = st.sidebar.columns([5,2])
credit_card = col1.checkbox("Credit Card")
col1, col2  = st.sidebar.columns([5,2])
payment_refund = col1.checkbox("Payment Refund")
st.sidebar.write("", unsafe_allow_html=True)

#ROOM VIEW
st.sidebar.write("<h3>Room View</h3>", unsafe_allow_html=True)
col1, col2  = st.sidebar.columns([5,2])
garden_view = col1.checkbox("Garden View")
col1, col2  = st.sidebar.columns([5,2])
lake_view = col1.checkbox("Lake View")
col1, col2  = st.sidebar.columns([5,2])
city_view = col1.checkbox("City View")
st.sidebar.write("", unsafe_allow_html=True)







#st.markdown("<h2 style='text-align:left; font-weight:bold;'>Yeni Bir Kullanıcı İçin Tahmin Yapalım</h2>", unsafe_allow_html=True)



#if page == "Page_1":
#st.markdown("<h1 style='text-align:center;'>Miuul DSMLBC11 Blackbox Grubu Streamlit Eğitimi</h1>", unsafe_allow_html=True)
#st.markdown("<h2 style='text-align:center;'>Açılış Sayfası</h2>", unsafe_allow_html=True)
#st.write(       """Bu site Miuul DSMLBC11 Blackbox Grubu Streamlit Eğitimi için hazırlanmıştır.""")
#st.write(        """Site 3 sayfadan oluşmaktadır. Sayfalara sol menüden erişebilirsiniz.""")
#st.write("""1. Açılış Sayfası""")
#st.write("""2. Keşifsel Veri Analizi Sayfası""")
#st.write("""3. Tahminleme Sayfası""")









