import nltk
from nltk.chat.util import Chat, reflections
pairs = [

   #housing faq url: https://www.swosu.edu/administration/reslife/faqs.aspx
    
    [
        r"(.*) apply (.*) campus",
        ["Q: Who may apply for housing on the SWOSU campus? /n A: University housing is available for current SWOSU students, faculty, and staff only.",]
    ],
    [
        r"(.*) housing time| how long ?",
        ["Q: How long is the housing term for which I am signing up for? /n A: Housing accommodations are available in a 9-month  academic term and/or a 3-month summer term. /n Space is often limited and reserved on a first-come, first-served basis.",]
    ],
    [
        r"(.*)housing (.*) Payment options",
        ["Q: What are my housing payment options? /n A: You can make payments all at once or in four installments. /n  Any further questions, please contact the business office at 580.774.3019.",]
    ],
    [
        r"(.*) purchase|buy (.*) meal plan",
        ["Q: Must meal plans be purchased? /n A:A meal plan must be purchased if you live in a Residence Hall.",]
    ],
    [
        r"(.*) private room ?",
        ["Q:Can I get a private room?  /n A: Private rooms are assigned as space permits and are allotted on a seniority basis for all returning residents. /n All new applicants are given priority according to completed deposit and reservation agreement. Email requests to reslife@swosu.edu. ",]
    ],
    [
        r"(.*) cancel (.*) housing",
        ["Q: What if I change my mind? (housing) /n A:You are free to change your mind and receive your refunded deposit anytime before the cancellation deadline on the contract. /n Cancellation after the deadline will result in a forfeit of the deposit. /n Once a resident officially checks into his/her residence, he/she is bound to fulfill the full term and cancellation would then require an opt-out fee. Email requests to reslife@swosu.edu.  ",]
    ],

    [
        r"when (.*)  assignment|roommate",
        ["Q: When will I know my housing assignment and roommate? /n A: Emails will be sent to the residents SWOSU student email account by June 15. /n The email will give room number, roommate name and the roommate’s phone number.",]
    ],
    [
        r"(.*) choose (.*) roommate",
        ["Q: If my friend and I want to be roommates, what should we do? /n A:On the application (back), make sure to fill out the roommate questionnaire. /n Put your roommate request AND fill out description/expectations. /n Note: Do this ASAP because once assignments are made it is difficult to make changes.",]
    ],
    [
        r"(.*) change (.*) meal plan|room assignment|roommate|building",
        ["Q: How do I make changes for meal plans, room assignments, roommates or to switch buildings? /n A: Email your request to reslife@swosu.edu OR go to the Residence Life Office (located at southwest corner of Neff Hall under the blue awning).",]
    ],
    [
        r"(.*) ID card ?",
        ["Q: Where and for what can I use my ID card? /n A: The ID card can be used at the Duke's Diner (cafeteria), /n University Grill, Beanery (located in student union), Freshens (located in the wellness center), University Market (also known as the C-store, /n located next to the bookstore), and vending machines in the buildings for food/dining purposes. ID cards can also be used to get into SWOSU games/activities and Wellness Center for free.",]
    ],
    [
        r"(.*) park",
        ["Q: Where do I park and do I need a parking permit? /n A: There is parking available around each building. Students do need a parking permit, which they can get at campus police (located at the southeast corner of campus). /n Make sure to take Student ID, license plate number, and the make/model of the vehicle.",]
    ],
   #swosu alert FAQ url: https://www.swosu.edu/resources/alert-faq.aspx



    [
        r"who (.*) register (.*) alerts",
        ["Q: Who can register for SWOSU Alert? /n A: The SWOSU Alert service is designed for students, /n faculty and staff who will be affected directly by an emergency on the University grounds and/or the proximate areas. /n Registrants may add an additional phone number or email address, so that a friend or family member is notified of an emergency.",]
    ],
    [
        r"why (.*) register (.*) alerts",
        ["Q: Why should I register for SWOSU Alert? /n A: Text messaging is more reliable in emergency situations when communication systems reach high capacity. /nText messages will get through when phone calls won't. /nYou will receive alerts anywhere, even when you do not have access to a computer.",]
    ],
        
    [
        r"number (.*) confidential",
        ["Q: Will my mobile phone number be kept confidential? /n A: Yes. Mobile phone numbers submitted to the SWOSU Alert service are not shared or sold to any other systems or services.",]
    ],
    [
        r"how many (.*) messegaes (.*)",
        ["Q: How many SWOSU Alert text messages will I receive? /n A: SWOSU Alert text messages will be sent only to alert you to emergency situations in which there is an imminent threat to public safety or for campus closures due to inclement weather. /nThe exact number is difficult to predict, but there should be very few.",]
    ],
        
    [
        r"(.*) register|cost|price (.*) Alert",
        ["Q: What is required to register for SWOSU Alert and how much does it cost? /n A: All you need is a mobile phone with text messaging capabilities if you wish to receive emergency text messages. There is no charge to users for signing up. /nIndividual mobile phone plans will apply normal charges for the text message. If you are interested in receiving the emergency messages through email only, all you need is an email account.",]
    ],
        
    [
        r"(.*) change (.*) service|provider",
        ["Q: What if I change my mobile phone service provider? /n A: To change mobile phone service providers, log into your SWOSU Alert account. In the \"Services\" area, /nclick \"Change Status\" which is located to the right of your mobile phone number. /nSelect the new mobile phone service provider and click the \"Update Phone\" button.",]
    ],
        
    [
        r"(.*) apply|sign up (.*) alert",
        ["Q: How do I sign up for SWOSU Alert? /n A: To register to receive text messages, you do need to have your mobile phone handy. /nComplete the online form. You will be asked to create your own username and password. /n(Note: It is recommended that you use your SWOSU username associated with your SWOSU email account--what appears in front of the @) You will receive a text message that will include a 4-digit validation code. /nYou must enter the validation code on the confirmation web page and hit the \"Validate\" button. You will then automatically be forwarded to a \"Thank You\" page. /nThe validate button also creates your own personal account where you should go next and enter your preferred email address. /nThis is where you will log in to update personal contact information. If you would like to receive emergency messages through email only, click the link on the online form indicating you wish to sign up for email only.",]
    ],
        
    [
        r"(.*) not able|unable (.*) register",
        ["Q: What if I am not able to register? /n A: For registration assistance, email your mobile phone number and the name of your provider to support@e2Campus.com. /nIndicate you want to register in the SWOSU Alert system at Southwestern Oklahoma State University.",]
    ],
        
    [
        r"(.*) opt-out|discontinue (.*) alert",
        ["Q: How can I opt-out of SWOSU Alert? /n A: You can opt-out (discontinue) at any time just as quickly and easily as you signed up. Log in to your SWOSU Alert account. /nIn the \"Services\" area, click \"Change Status\" which is located to the right of your mobile phone number. /nSelect the \"Inactive\" option and click the \"Update Active State\" button.",]
    ],
        
    [
        r"(.*) alert (.*) tell",
        ["Q: What will the SWOSU Alert tell me? /n A: A short text message will state there is an emergency and /nindicate the suggested action or that there is a campus closure due to inclement weather.",]
    ],
        
    [
        r"(.*) find (.*) answer",
        ["Q: What if I didn't find my answer? /n A: You may contact the SWOSU helpdesk at 580.774.7070 for additional assistance.",]
    ],

#dukes diner faq url: https://www.swosu.edu/administration/auxservices/cafeteria/faqs.aspx

     [
        r"(.*) diner|eat|cafeteria (.*) sick|ill|illness ?",
        ["Q: What if I'm sick? (diner) /n A: You may obtain a sick tray if you are unable to go to the dining hall due to illness. /nYou must give your ID to a Residence Hall Advisor (RA) who will fill out the form required by the cashier. /nOnce the form is presented to the cashier, a sick tray will be prepared.",]
     ],
     [
        r"(.*) diet (.*)",
        ["Q: What if I need a special diet?(diner) /n A: If you have special needs concerning your diet, contact the Duke's Diner manager. /nWe can assist you in staying within your daily diet by offering foods that meet those requirements.",]
     ],
     [
        r"(.*) employment|job|work (.*) food|diner|cafeteria",
        ["Q: Is there employment in Food Services? /n A: Food Services employ 75 students in jobs ranging from cooking and serving to washing dishes. /nStudents work an average of 15 hours per week. If you are interested in employment, see the Food Service manager. /nThe work schedule coincides with the university calendar.",]
     ],
     [
        r"(.*) lend|borrow|give (.*) id|card",
        ["Q: Why can't I lend my ID card? /n A: The university ID card is encoded with each card holder's meal plan and must be presented to the dining hall checker at meal times. /nThe board portion of your room and board bill is partially based on the assumption that each resident with a meal contract will miss some meals. /nThe cost of the board portion would have to be raised to cover additional expenses incurred by serving more total meals. This assumption is the basis for the "no loan" policy dealing with the use of the student's ID card. /nThe meal contract is issued to one resident and may not be used by anyone other than the owner.",]
     ],

#HR faq url:

     [
        r"(.*) find (.*) jobs|job|wok|employment",
        ["Q: How do I find out what jobs are available at Southwestern Oklahoma State University? /n A: All Faculty, Staff and Student positions are listed on SWOSU’s online job page called “BulldogWorks.” To access this page, visit www.jobs.swosu.edu.  /nThis link can also be accessed from the SWOSU home page or under the Human Resources tab.  /nPositions are posted as they become available.  The Human Resources office hours are 8:00am-5:00pm.  /nFor any assistance or questions, contact the Employment Specialist at (580) 774-6012.",]
     ],
     [
        r"(.*) apply|application (.*) employment|job|jobs",
        ["Q: How do I complete an application and apply for employment at Southwestern Oklahoma State University? /n A: Applications are accepted online at www.jobs.swosu.edu.  A username and password are required to create an account in BulldogWorks.  Individuals must create an online account to apply for jobs.  /nDetails are included in each posting as well as the documents needed to apply.  /nTo apply for a posting, click the “Apply for this Job” button.  Please note SWOSU does not accept paper applications or unsolicited applications for Staff/Faculty positions. /nStudent jobs can be accessed at www.collegecentral.com/swosu.  Students must apply online through the Bulldog Job Board to be considered.  Visit Career Services, located in Stafford 209 or call (580) 774-3233 if you have any questions.",]
     ],
     [
        r"(.*) work study ?",
        ["Q: What is work study, and how do I know if I qualify for it? /n A: try this site: https://www.swosu.edu/administration/sfs/workstudy/index.aspx",]
     ],
     [
        r"(.*) new application (.*) job|position|work ?",
        ["Q: Is a new application required for each position of interest? /n A: Yes, a new online application is required for each job posting.  Once an individual has created an account in BulldogWorks, their information is saved for future applications.  /nHowever, individuals must login and submit an application for each position in or to be considered.",]
     ],
     
    

#misc.
    #using the word 'for' gives error, likely other pythonutity words do

    [
        r"evert sucks ?",
        ["I agree", "yup.", "totally.", "tell me about it."]
    ],
   """

default format for questions:
[
        r"(.*)",
        ["Q:  /n A: ",]
     ],
"""
    [
        r"(.*) created ?",
        ["Joeys, Caden, and Zack made this bot",]
    ],
    [
        r"(.*) (location|city) ?",
        ['weatherford, Oklahoma',]
    ],
   
    [
        r"(.*) (help) ?", #gives eror see note under misc.
        ["You may contact the SWOSU helpdesk at 580.774.7070 for additional assistance.",]
    ],
#generic response
    [
        r"(.*)",
        ["Sorry, I didn't catch that, please refrase your question.", "I might not have an answer for that."]
    ],


    [
        r"quit",
        ["Thank you"]
],
]
def Carl():
    print("Hi, Please ask your questions here. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    Carl()
