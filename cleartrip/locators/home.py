# ---- Flight
FROM = "//input[@name='origin']"
TO = "//input[@name='destination']"
DEPARTURE_DATE = "//input[@title='Depart date']"
CHILDREN_DROPDOWN = "//*[@id='Childrens']"
SEARCH_BUTTON = "//*[@value='Search flights']"

#--- booking

BOOK_FLIGHT = " //*[@class='resultUnit flightDetailsLink ']//*[@class='booking']"




#--- Itinarary
CHK_BOX_INSURANCE = "//*[@for='insurance_confirm']"
COUPON = "//input[@name='coupon']"
CONT_BUTTON = "//input[@id='itineraryBtn']"

#---travelerDetails
EMAIL = "//input[@type='email']"
CONT_BUTTON1 = "//input[@id='LoginContinueBtn_1']"
TITLE = "//select[@name='AdultTitle1']"
FNAME = "//input[@name='AdultFname1']"
LNAME = "//input[@name='AdultLname1']"
MB = "//input[@name='contact1']"
