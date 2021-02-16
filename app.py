import streamlit as st

option = st.sidebar.selectbox(
    'Select the app you want to use',
     ("House Price Prediction","BMI Calculation"))

if option=="House Price Prediction":

    st.title("House Price Estimate :house_buildings:")


    area = st.slider("Housing Area",1650,16200,5000)
    # st.write('Area:',area)

    bedrooms = st.selectbox('# of Bedrooms',(1,2,3,4,5,6,7))
    # st.write('Bedrooms:', bedrooms)

    bathrooms = st.selectbox('# of Bathrooms',(1,2,3,4))
    # st.write('Bathrooms:', bathrooms)

    stories = st.selectbox('# of Stories',(1,2,3,4))
    # st.write('Stories:', stories)

    mainroad = st.selectbox('Main Road',("Yes","No"))
    if mainroad == "Yes":
        main_road = 1
    else:
        main_road = 0
    # st.write('Main Road:', mainroad)

    guestroom = st.selectbox('Guest Room',("Yes","No"))
    if guestroom == "Yes":
        guest_room = 1
    else:
        guest_room = 0
    # st.write('Guest Room:', guestroom)

    hotwaterheating = st.selectbox('Hot Water Heating',("Yes","No"))
    if hotwaterheating == "Yes":
        hotwater_heating = 1
    else:
        hotwater_heating = 0
    # st.write('Hot Water Heating:', hotwaterheating)

    airconditioning = st.selectbox('Air Conditioning',("Yes","No"))
    if airconditioning == "Yes":
        air_cond = 1
    else:
        air_cond = 0
    # st.write('Air Conditioning:', airconditioning)

    parking = st.selectbox('No of Car Parking',(0,1,2,3))
    #st.write('No of Car Parking:', parking)

    prefarea = st.selectbox('Is area preferred ?',("Yes","No"))
    if prefarea == "Yes":
        pref_area = 1
    else:
        pref_area = 0
    # st.write('Is area preferred ?', prefarea)

    answer = (-332789.2) + (area * 2.401239e+02) + (bedrooms*1.526964e+05) + (bathrooms*1.144427e+06) + (stories*3.762286e+05) + (main_road*6.427429e+05) + (guest_room*4.404670e+05) + (hotwater_heating*1.035725e+06) + (air_cond*8.209643e+05) + (parking*2.453935e+05) + (pref_area*7.429601e+05)

    answer = round(answer,1)

    st.success("House price is: {} $".format(answer))

else:
    st.header("*BMI Calculator*  :sunglasses: :syringe:")


    weight = st.slider("Weight please (in KG)!!", 0, 200, 50, 1)
    height = st.slider("Height too (in m)", 0.00, 4.00, 1.00, 0.01)

    def BMI_Calculator(w,h):
        return(w/(h**2))

    if st.button('BMI_Calculator'):
        try:
            result_1 = BMI_Calculator(weight,height)
            st.text(result_1)
            if result_1 <18.50:
                st.text("Your BMI is considered underweight, so please eat something!!!")
            elif result_1 <24.9:
                st.text("Your BMI is considered normal!!")
            elif result_1 <29.9:
                st.text("Your BMI is considered overweight!!")
            else:
                st.text("Your BMI is considered obese!!")
                
        except:
            st.text("Get a life!!")
