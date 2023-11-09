import streamlit as st

st.title('Title -> Hello Everyone.')                          # Title
st.header('Header -> Hello Everyone.')                        # Header
st.subheader('SubHeader -> Hello Everyone.')                  # Sub header
st.text('Text -> Hello Everyone.')                            # Text

st.markdown('# Hi')                                           # Markdown
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')

st.success('Success!')                                        # Success
st.info('Information!')                                       # Info
st.warning('Warning!')                                        # Warning
st.error('Error!')                                            # Error

st.exception(ZeroDivisionError('Division not possible'))      # Exception

st.help(ZeroDivisionError)                                    # Help

st.write('1+2+3')                                             # Write
st.write(1+2+3)

st.code('x=10\n'                                              # Code
        'for i in range(x):\n'
        '\tprint(i)')

st.checkbox('Male')                                           # Checkbox

if(st.checkbox('Adult')):
    st.write("You're an Adult.")

radioButton = st.radio('Select: ',('Male','Female','Other'))  # Radio

if radioButton == 'Male':
    st.write('You are Male.')
elif radioButton == 'Female':
    st.write('You are Female.')
elif radioButton == 'Other':
    st.write('You are Other.')

st.subheader('Select Box')                                    # Select box
selectBox = st.selectbox('Data Science : ',['Data Analysis','Web Scraping','Machine Learning',
                                            'Natural Language Processing','Computer Vision',
                                            'Deep Learning','Image Processing',])
st.write('You have selected : ', selectBox)


st.subheader('MultiSelect Box')                              # MultiSelect box
MultiSelect = st.multiselect('Data Science : ',['Data Analysis','Web Scraping','Machine Learning',
                                                'Natural Language Processing','Computer Vision',
                                                'Deep Learning','Image Processing',])
st.write('You have selected : ', len(MultiSelect), 'Courses')


st.subheader('Button')                                    # Button
st.button('Click me')

st.subheader('Slider')                                    # Slider
vol = st.slider('Select the level : ',0,100,step=1)
st.write('Volume is : ', vol)

st.subheader('Text Input')                                # Text Input
username = st.text_input('Username : ')
password = st.text_input('Password : ',type='password')

st.subheader('Text Area')                                # Text Area
st.text_area('Write something')


st.subheader('Input Number')                              # Input Number
st.number_input('Input your age : ',18,110)

st.subheader('Input Date')                                # Input Date
st.date_input('Input Date : ')

st.subheader('Input Time')                                # Input Time
st.time_input('Enter time : ')
