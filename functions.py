import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 250)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

df = pd.read_excel("C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/hotel_info_2_bet.xlsx")


hotel = pd.read_excel("C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/hotel_info_2_bet.xlsx", sheet_name="hotel")
ratings = pd.read_excel("C:/Users/Lenovo/PycharmProjects/pythonProject/MY_LUDW_PROJECT/streamlit_canli/hotel_info_2_bet.xlsx", sheet_name="ratings")

df_ = pd.merge(hotel,ratings, how="left", on=["hotel_id"])
df = df_.copy()
df.head()

df.shape
df.isnull().sum()

def content_based_recommender(hotel_name, cosine_sim, dataframe):
    indices = pd.Series(dataframe.index, index=dataframe['hotel_name_x'])
    indices = indices[~indices.index.duplicated(keep='last')]
    hotel_index = indices[hotel_name]
    similarity_scores = pd.DataFrame(cosine_sim[hotel_index], columns=["scores"])
    similarity_scores = similarity_scores.reset_index()
    similarity_scores = similarity_scores.rename(columns={"index": "hotel_index"})
    similarity_scores = similarity_scores.sort_values("scores", ascending=False)
    recommended_indices = similarity_scores[similarity_scores["hotel_index"] != hotel_index]["hotel_index"]
    recommended_hotels = dataframe.loc[recommended_indices, :]
    return recommended_hotels

def calculate_cosine_sim(dataframe):
    tfidf = TfidfVectorizer(stop_words='english')
    dataframe['reviews'] = dataframe['reviews'].fillna('')
    tfidf_matrix = tfidf.fit_transform(dataframe['reviews'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# Assuming you have defined df as your dataframe

cosine_sim = calculate_cosine_sim(df)
recommended_hotels = content_based_recommender('Komfort Hotel Ludwigsburg', cosine_sim, df)
recommended_hotels = recommended_hotels[recommended_hotels['hotel_name_x'] != 'Schlosshotel Monrepos']
recommended_hotels = recommended_hotels['hotel_name_x'].unique()
print(recommended_hotels)



####
##feature engineering

df2 = pd.read_excel("datasets/hotel_info.xlsx")
df2.head()

hotels = pd.read_excel("datasets/hotel_info.xlsx", sheet_name="hotel")
hotels.head()
def grab_col_names(dataframe, cat_th=10, car_th=20):
    """

    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ------
        dataframe: dataframe
                Değişken isimleri alınmak istenilen dataframe
        cat_th: int, optional
                numerik fakat kategorik olan değişkenler için sınıf eşik değeri
        car_th: int, optinal
                kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    ------
        cat_cols: list
                Kategorik değişken listesi
        num_cols: list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_cat cat_cols'un içerisinde.
        Return olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols + cat_but_car = değişken sayısı

    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(hotels)
hotels["type (Hotel, Pension, guesthouse, Youth Hostel, riding house"].value_counts()


##############################RECOMMEND PART############################
def content_based_recommender(hotel_name, cosine_sim, dataframe):
    indices = pd.Series(dataframe.index, index=dataframe['hotel_name_x'])
    indices = indices[~indices.index.duplicated(keep='last')]
    hotel_index = indices[hotel_name]
    similarity_scores = pd.DataFrame(cosine_sim[hotel_index], columns=["scores"])
    similarity_scores = similarity_scores.reset_index()
    similarity_scores = similarity_scores.rename(columns={"index": "hotel_index"})
    similarity_scores = similarity_scores.sort_values("scores", ascending=False)
    recommended_indices = similarity_scores[similarity_scores["hotel_index"] != hotel_index]["hotel_index"]
    recommended_hotels = dataframe.loc[recommended_indices, :]
    return recommended_hotels

def calculate_cosine_sim(dataframe):
    tfidf = TfidfVectorizer(stop_words='english')
    dataframe['reviews'] = dataframe['reviews'].fillna('')
    tfidf_matrix = tfidf.fit_transform(dataframe['reviews'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# Assuming you have defined df as your dataframe

cosine_sim = calculate_cosine_sim(df)
recommended_hotels = content_based_recommender('Schlosshotel Monrepos', cosine_sim, df)
recommended_hotels = recommended_hotels[recommended_hotels['hotel_name_x'] != 'Schlosshotel Monrepos']
recommended_hotels = recommended_hotels['hotel_name_x'].unique()
print(recommended_hotels)



###########BREAKFAST#########
import streamlit as st

# Otel verilerini içeren bir liste
hotels = hotel
hotels.head()

def recommend_hotel_with_breakfast():
    # Kahvaltı seçeneği varsa kahvaltı dahil otelleri filtrele
    breakfast_hotels = [hotel for hotel in hotels if hotel["breakfast"]]

    # Filtrelenen otelleri fiyat ve rating'e göre sırala
    sorted_hotels = sorted(breakfast_hotels, key=lambda x: (x["weekdays_price"]), reverse=True)

    # En iyi oteli öner
    recommended_hotel = sorted_hotels[0]

    return recommended_hotel


def recommend_hotel_without_breakfast():
    # Kahvaltı seçeneği yoksa tüm otelleri fiyat ve rating'e göre sırala
    sorted_hotels = sorted(hotels, key=lambda x: (x["weekdays_price"]), reverse=True)

    # En iyi oteli öner
    recommended_hotel = sorted_hotels[0]

    return recommended_hotel




########BREAKFAST VE RESTAURANT####
import streamlit as st

# Otel verilerini içeren bir liste
hotels = [
    {
        "name": "Hotel A",
        "breakfast": True,
        "restaurant": True,
        "price": 100,
        "rating": 4.5
    },
    {
        "name": "Hotel B",
        "breakfast": False,
        "restaurant": True,
        "price": 80,
        "rating": 4.2
    },
    {
        "name": "Hotel C",
        "breakfast": True,
        "restaurant": False,
        "price": 120,
        "rating": 4.8
    }
]


def recommend_hotel(breakfast_option, restaurant_option):
    # Kahvaltı ve restoran seçeneklerine göre otelleri filtrele
    filtered_hotels = [hotel for hotel in hotels if
                       hotel["breakfast"] == breakfast_option and hotel["restaurant"] == restaurant_option]

    # Filtrelenen otelleri fiyat ve rating'e göre sırala
    sorted_hotels = sorted(filtered_hotels, key=lambda x: (x["price"], x["rating"]), reverse=True)

    # En iyi oteli öner
    recommended_hotel = sorted_hotels[0]

    return recommended_hotel


# Streamlit uygulaması
def main():
    st.title("Otel Tavsiye Sistemi")
    st.write("Kahvaltı ve restoran seçeneği ile otel tavsiye edin")

    breakfast_option = st.checkbox("Kahvaltı seçeneği var mı?")
    restaurant_option = st.checkbox("Restoran seçeneği var mı?")

    recommended_hotel = recommend_hotel(breakfast_option, restaurant_option)

    st.subheader("Önerilen Otel")
    st.write("İsim:", recommended_hotel["name"])
    st.write("Fiyat:", recommended_hotel["price"])
    st.write("Rating:", recommended_hotel["rating"])


if __name__ == "__main__":
    main()
