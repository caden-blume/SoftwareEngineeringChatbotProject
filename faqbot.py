import nltk
from nltk.chat.util import Chat, reflections
pairs = [

   #housing faq url: https://www.swosu.edu/administration/reslife/faqs.aspx
   
    [
        r"(.*) apply (.*) campus",
        ["Q: Who may apply for housing on the SWOSU campus? A: University housing is available for current SWOSU students, faculty, and staff only.",]
    ],
    [
        r"(.*) housing time| how long ?",
        ["Q: How long is the housing term for which I am signing up for? A: Housing accommodations are available in a 9-month  academic term and/or a 3-month summer term. Space is often limited and reserved on a first-come, first-served basis.",]
    ],
    [
        r"(.*)housing (.*) Payment options",
        ["Q: What are my housing payment options?  A: You can make payments all at once or in four installments.  Any further questions, please contact the business office at 580.774.3019.",]
    ],
    [
        r"(.*) purchase|buy (.*) meal plan",
        ["Q: Must meal plans be purchased? A:A meal plan must be purchased if you live in a Residence Hall.",]
    ],
    [
        r"(.*) private room ?",
        ["Q:Can I get a private room? A: Private rooms are assigned as space permits and are allotted on a seniority basis for all returning residents. All new applicants are given priority according to completed deposit and reservation agreement. Email requests to reslife@swosu.edu. ",]
    ],
    [
        r"(.*) cancel (.*) housing",
        ["Q: What if I change my mind? (housing) A:You are free to change your mind and receive your refunded deposit anytime before the cancellation deadline on the contract. Cancellation after the deadline will result in a forfeit of the deposit. Once a resident officially checks into his/her residence, he/she is bound to fulfill the full term and cancellation would then require an opt-out fee. Email requests to reslife@swosu.edu.  ",]
    ],

    [
        r"when (.*)  assignment|roommate",
        ["Q: When will I know my housing assignment and roommate? A: Emails will be sent to the residents SWOSU student email account by June 15. The email will give room number, roommate name and the roommate’s phone number.",]
    ],
    [
        r"(.*) choose (.*) roommate",
        ["Q: If my friend and I want to be roommates, what should we do? A:On the application (back), make sure to fill out the roommate questionnaire. Put your roommate request AND fill out description/expectations. Note: Do this ASAP because once assignments are made it is difficult to make changes.",]
    ],
    [
        r"(.*) change (.*) meal plan|room assignment|roommate|building",
        ["Q: How do I make changes for meal plans, room assignments, roommates or to switch buildings? A: Email your request to reslife@swosu.edu OR go to the Residence Life Office (located at southwest corner of Neff Hall under the blue awning).",]
    ],
    [
        r"(.*) ID card ?",
        ["Q: Where and for what can I use my ID card? A: The ID card can be used at the Duke's Diner (cafeteria), University Grill, Beanery (located in student union), Freshens (located in the wellness center), University Market (also known as the C-store, located next to the bookstore), and vending machines in the buildings for food/dining purposes. ID cards can also be used to get into SWOSU games/activities and Wellness Center for free.",]
    ],
    [
        r"(.*) park|parking (.*) orientation",
        ["Q: Where do I park and do I need a parking permit? A: There is parking available around each building. Students do need a parking permit, which they can get at campus police (located at the southeast corner of campus). Make sure to take Student ID, license plate number, and the make/model of the vehicle.",]
    ],
   #swosu alert FAQ url: https://www.swosu.edu/resources/alert-faq.aspx



    [
        r"who (.*) register (.*) alerts",
        ["Q: Who can register for SWOSU Alert? A: The SWOSU Alert service is designed for students, faculty and staff who will be affected directly by an emergency on the University grounds and/or the proximate areas. Registrants may add an additional phone number or email address, so that a friend or family member is notified of an emergency.",]
    ],
    [
        r"why (.*) register (.*) alerts",
        ["Q: Why should I register for SWOSU Alert? /n A: Text messaging is more reliable in emergency situations when communication systems reach high capacity. /nText messages will get through when phone calls won't.You will receive alerts anywhere, even when you do not have access to a computer.",]
    ],
        
    [
        r"number (.*) confidential",
        ["Q: Will my mobile phone number be kept confidential?  A: Yes. Mobile phone numbers submitted to the SWOSU Alert service are not shared or sold to any other systems or services.",]
    ],
    [
        r"how many (.*) messegaes (.*)",
        ["Q: How many SWOSU Alert text messages will I receive? A: SWOSU Alert text messages will be sent only to alert you to emergency situations in which there is an imminent threat to public safety or for campus closures due to inclement weather.The exact number is difficult to predict, but there should be very few.",]
    ],
        
    [
        r"(.*) register|cost|price (.*) Alert",
        ["Q: What is required to register for SWOSU Alert and how much does it cost? A: All you need is a mobile phone with text messaging capabilities if you wish to receive emergency text messages. There is no charge to users for signing up.Individual mobile phone plans will apply normal charges for the text message. If you are interested in receiving the emergency messages through email only, all you need is an email account.",]
    ],
        
    [
        r"(.*) change (.*) service|provider",
        ["Q: What if I change my mobile phone service provider? A: To change mobile phone service providers, log into your SWOSU Alert account. In the \"Services\" area, click \"Change Status\" which is located to the right of your mobile phone number. Select the new mobile phone service provider and click the \"Update Phone\" button.",]
    ],
        
    [
        r"(.*) apply|sign up (.*) alert",
        ["Q: How do I sign up for SWOSU Alert?  A: To register to receive text messages, you do need to have your mobile phone handy. Complete the online form. You will be asked to create your own username and password. (Note: It is recommended that you use your SWOSU username associated with your SWOSU email account--what appears in front of the @) You will receive a text message that will include a 4-digit validation code. You must enter the validation code on the confirmation web page and hit the \"Validate\" button. You will then automatically be forwarded to a \"Thank You\" page. The validate button also creates your own personal account where you should go next and enter your preferred email address. This is where you will log in to update personal contact information. If you would like to receive emergency messages through email only, click the link on the online form indicating you wish to sign up for email only.",]
    ],
        
    [
        r"(.*) not able|unable (.*) register",
        ["Q: What if I am not able to register?  A: For registration assistance, email your mobile phone number and the name of your provider to support@e2Campus.com. Indicate you want to register in the SWOSU Alert system at Southwestern Oklahoma State University.",]
    ],
        
    [
        r"(.*) opt-out|discontinue (.*) alert",
        ["Q: How can I opt-out of SWOSU Alert?  A: You can opt-out (discontinue) at any time just as quickly and easily as you signed up. Log in to your SWOSU Alert account. In the \"Services\" area, click \"Change Status\" which is located to the right of your mobile phone number. Select the \"Inactive\" option and click the \"Update Active State\" button.",]
    ],
        
    [
        r"(.*) alert (.*) tell",
        ["Q: What will the SWOSU Alert tell me?  A: A short text message will state there is an emergency and indicate the suggested action or that there is a campus closure due to inclement weather.",]
    ],
        
    [
        r"(.*) find (.*) answer",
        ["Q: What if I didn't find my answer?  A: You may contact the SWOSU helpdesk at 580.774.7070 for additional assistance.",]
    ],

#dukes diner faq url: https://www.swosu.edu/administration/auxservices/cafeteria/faqs.aspx

     [
        r"(.*) diner|eat|cafeteria (.*) sick|ill|illness ?",
        ["Q: What if I'm sick? (diner)  A: You may obtain a sick tray if you are unable to go to the dining hall due to illness. You must give your ID to a Residence Hall Advisor (RA) who will fill out the form required by the cashier. /nOnce the form is presented to the cashier, a sick tray will be prepared.",]
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
        ["Q: Why can't I lend my ID card? /n A: The university ID card is encoded with each card holder's meal plan and must be presented to the dining hall checker at meal times. /nThe board portion of your room and board bill is partially based on the assumption that each resident with a meal contract will miss some meals. /nThe cost of the board portion would have to be raised to cover additional expenses incurred by serving more total meals. This assumption is the basis for the \"no loan\" policy dealing with the use of the student's ID card. /nThe meal contract is issued to one resident and may not be used by anyone other than the owner.",]
     ],

#HR faq url: https://www.swosu.edu/administration/hr/faqs.aspx

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
     
    #NSO FaQ url: https://www.swosu.edu/admissions/nso/faqs.aspx
     [
        r"what (.*) nso|new student orientation",
        ["Q: What is New Student Orientation (NSO)? /n A: New Student Orientation includes an Orientation Session prior to the beginning of the fall semester, /nMass Orientation, a one-hour freshman orientation course, and Dawg Days (planned activities during the first few weeks of the fall semester).",]
     ],
     [
        r"(.*) ol|orientaion leader",
        ["Q: What is an OL? /n A: More than 50 student Orientation Leaders (OLs) help freshmen and their families smooth the transition from high school to college. /nOLs are selected through an application and interview process and participate in a two-hour student leadership course each semester before working with new students. /nOLs also team teach the freshman orientation course with a SWOSU faculty or staff member that all new freshmen take.",]
     ],
     [
        r"how (.*)freshman|total enroll|enrollment",
        ["Q: How many freshmen enroll each year? What is the total enrollment? /n A: More than 900 freshmen enroll each year. SWOSU’s total enrollment is close to 5,000.",]
     ],
     [
        r"what (.*) orientation|orientation session",
        ["Q: What is an orientation session? /n A: Students meet as a group and get information about enrollment procedures and campus. Then the students divide into smaller groups according to the major they plan to pursue. /nThese smaller groups meet with an academic advisor in their academic field. The advisor helps the student choose classes, build a schedule and enroll. /nOrientation Leaders are also on hand to provide assistance and answer questions about life at SWOSU.",]
     ],
     [
        r"(.*)orientation (.*) schedule|scheduled",
        ["Q: How many orientation sessions are scheduled? /n A: Each year we have a total of six sessions: April 5, April 11, April 17, June 17, July 15 and August 14. All sessions begin at 9 a.m.",]
     ],
     [
        r"when|how (.*) register (.*) orientation ",
        ["Q: When do I register for an Orientation Session? /n A: You may register for an Orientation Session after you have completed the online application for University Admission and received written notification of acceptance to SWOSU. /nWithin the acceptance packet, you will find New Student Orientation information. Select an Orientation Session and register online or by phone, 580.774 3233. You will receive confirmation via email after we receive your reservation. /nSessions do fill quickly so register early.",]
     ],
     [
        r"(.*)cost|price (.*) orientation",
        ["Q: What is the cost for New Student Orientation? /n A: The New Student Orientation fee is $5 and will be added to the student's first semester’s bill.",]
     ],
     [
        r"(.*) attend (.*) session",
        ["Q: How many students attend each session? /n A: Up to 200 students may attend Orientation Sessions. /nHowever, students divide into smaller groups to enroll. Since we do have to limit the sessions, be sure to sign up early to reserve your spot!",]
     ],
    
     [
        r"(.*)families attend ?",
        ["Q: May families attend? /n A: We encourage families to attend Family Orientation Sessions while students attend their orientation session. /nFamily sessions run concurrently with student orientation sessions and are designed to answer parental questions and concerns. /nFamilies do not attend the Student Orientation Session or go with their student to enroll in classes.",]
     ],
     [
        r"(.*)orientation required",
        ["Q: Is orientation required of all students? /n A: Orientation is required of all first-time entering freshmen. /nThe student receives one hour of credit for attending the enrollment session, Mass Orientation, and the freshman orientation course in the fall.",]
     ],
     [
        r"(.*)do (.*) orientation",
        ["Q: What else can I do at the orientation session? /n A: While you wait for your printed course schedule, you can get your SWOSU student ID and parking decal (bring a photo ID). /nYou can also tour the campus and residence halls, and talk with new and current students, and attend the open house. /nIt is recommended that you take Computerized Placement Tests (CPT) while on campus for NSO. You must have photo ID to take CPT tests.",]
     ],
     [
        r"(.*)happens|do (.*) open house",
        ["Q: What happens at the Open House during orientation sessions? /n A: The Open House is another opportunity to find answers and learn more about student services. Participating offices include: Financial Services, Residence Life, Human Resources, Business Offices, Campus Police, Student Union and Food Services (meal plans), Counseling and Health Services and Dean of Students. Representatives can answer questions concerning meal plans, residence hall contracts, tuition and other payments, campus jobs, health forms and financial assistance.",]
     ],
     [
        r"what (.*)cpt ?",
        ["Q: What is a CPT exam? /n A: CPT stands for Computerized Placement Test. Students with ACT sub-scores (math, reading and English) below 19 must enroll in remedial courses. /nYou may take a CPT to clear the deficiency in any or all areas. /nThere is no charge to take CPTs. You may take each test twice; however, there is a two-week waiting period between testing sessions. /nTo schedule CPT testing, contact the Assessment Office at 580.774.7084. *Results are immediate.",]
     ],
     [
        r"when (.*) cpt",
        ["Q: When should I take the CPT exam? /n A: It is best to take the CPT exam before attending an orientation session. However, you may also schedule exams the morning or afternoon of your orientation session. /nStudents must enroll in remedial courses until clearing (passing) deficient subject area(s). Upon successful completion of CPTs, students may change their schedules. /nContact New Student Orientation in Stafford 209 or call 580.774.3233 for the schedule change process.",]
     ],
     [
        r"(.*) dawg days",
        ["Q: What are Dawg Days? /n A: Dawg Days are fun-filled weeks of activities designed to help students meet other students and become a part of our campus community. /nIt begins on Move-In Day and continues through the next several weeks. /nActivities include volleyball tournaments, dances, block party, tours, organizational fair, national speakers, Project Blue and much more!",]
     ],
     [
        r"(.*)mass orientation",
        ["Q: What is Mass Orientation? /n A: This is the first and only time all incoming freshmen meet as a group. /nAll freshmen are required to attend Mass O on August 17. During Mass O, you will be welcomed to SWOSU, learn some of our long-standing traditions, get a free freshman class t-shirt and take a freshman class picture.",]
     ],
     [
        r"happens|do (.*) freshman orientation",
        ["Q: What happens in the Freshman Orientation course? /n A: Volunteer instructors (SWOSU faculty, administrators and staff) paired with trained Orientation Leaders present information and college success skills each week. /nA large component of the class is designed to help students connect with the faculty, staff and other students.",]
     ],
     
     [
        r"when (.*)move (.*) hall|dorm",
        ["Q: When can I move into my residence hall? /n A: Fall Semester: The first day you can move into your hall is Thursday, August 15th at 9 a.m. /nVarious campus and community organizations welcome and help students move in.",]
     ],
     [
        r"(.*) find (.*)schedule|courses",
        ["Q: How do I find the course schedule? /n A: From the SWOSU homepage, scroll all the way to the bottom of the page, and click on “Class Schedules.” Select the term code (Fall, Spring or Summer) and the department to look up available days and times.",]
     ],
     [
        r"how (.*) change (.*) scehdule|class",
        ["Q: How can I change my schedule? /n A: Add/Drop Process for Freshman (Students with less than 30 completed credit hours) /nTo ensure that freshman receive proper guidance, the university requires that all freshman students meet with their advisor before making any schedule changes during the add/drop period (start of enrollment period until the 10th class day of the Fall/Spring Semester and start of enrollment period /nuntil the fifth class day in the Summer Semester). /nFreshman are unable to enroll online and can only make schedule changes in the Registrar’s Office during the add/drop period when he/she has their faculty advisor sign an Add/Drop form.",]
     ],
     [
        r"(.*)what classes (.*)",
        ["Q: How do I know what classes I need to take? /n A: All students must complete general education requirements and it is recommended to start with general education courses. /nAll students will meet with advisors during orientation session who review specific requirements for different areas of study. To find a complete list of degree information by major go to https://www.swosu.edu/resources/catalog/index.aspx",]
     ],
     [
        r"(.*)classes begin ?",
        ["Q: When do classes begin? /n A: Fall Semester: Classes begin Monday, August 19.",]
     ],
     [
        r"(.*)bring (.*) nso ?",
        ["Q: What do I need to bring to NSO? /n A: New Students: /nPhoto ID or Drivers License – Students should bring a photo ID with them to pick up their SWOSU student ID and parking decal or to take the CPT (Computerized Placement Test) to clear deficiencies./nFinal high school transcript (send at the end of the semester if grades have not posted/nStudent Health form/shot record/nResidence Hall application and $100 deposit)/nAny needed paper work for Financial Aid/nList of possible classes you would enjoy taking. Go to the online course schedule to view course selection and closed classes./nView the course catalog to find requirements for your academic major./nMoney for lunch. Feel free to grab lunch on or off campus. On-campus choices include Duke’s Diner, all-you-can-eat cafeteria, or the Food Court, four fast food outlets and a bakery. Food Court choices include Arrezzio's Italian Café, Brandy's Grill (hamburgers and sandwiches), Casa Solana Mexican Cantina, The Strip Joint (chicken strips and fries), The Corner Bakery (homemade baked goods) and Brandy's Grab-n-Go./n TRANSFER STUDENTS: /nPhoto ID or Drivers License – Students should bring a photo ID with them to pick up their SWOSU student ID and parking decal or to take the CPT (Computerized Placement Test) to clear deficiencies./nFinal college transcript (send at the end of the semester if grades have not posted)/nStudent Health form/shot record/nResidence Hall application and $100 deposit/nAny needed paper work for Financial Aid/nList of possible classes you would enjoy taking. Go to the online course schedule to view course selection and closed classes./nView the course catalog to find requirements for your academic major./nMoney for lunch. Feel free to grab lunch on or off campus. On-campus choices include Duke’s Diner, all-you-can-eat cafeteria, or the Food Court, four fast food outlets and a bakery. Food Court choices include Arrezzio's Italian Café, Brandy's Grill (hamburgers and sandwiches), Casa Solana Mexican Cantina, The Strip Joint (chicken strips and fries), The Corner Bakery (homemade baked goods) and Brandy's Grab-n-Go.",]
     ],
     [
        r"(.*)park (.*) ?",
        ["Q: Where do I park? /n A: Parking is available in front of the Fine Arts Center or at the Pioneer Cellular Event Center located at 900 N. 7th Street.",]
     ],
    


#fag camp duke url: https://www.swosu.edu/admissions/nso/camp-duke/faq.aspx




     [
        r"(.*) camp duke (.*) cost|price ",
        ["Q: How much does Camp Duke cost?   A: $200 and this includes all meals, t-shirt, activities and three nights stay.",]
     ],
     [
        r"(.*) pay (.*) camp duke ",
        ["Q: How do I pay for Camp Duke?   A: You will pay via credit card within the registration form.",]
     ],
     [
        r"(.*) camp duke (.*) enroll|enrollment|register|registration ",
        ["Q: When is the last day to enroll for Camp Duke?   A: SWOSU has space for 200 campers, registration will end on June 19, 2020 at 5 p.m. or when the 200 camper capacity is filled.",]
     ],
     [
        r"(.*) change (.*) camp duke ",
        ["Q: What if my plans change and I cannot come to Camp Duke?  A: If you decide not to come to Camp Duke, you can receive a full refund if you cancel your registration prior to June 26, 2020. For any cancellations after June 26th, no refunds will be given.",]
     ],
     [
        r"(.*) time (.*) camp duke (.*) start ? ",
        ["Q: What time does Camp Duke start?  A: Check-in begins at 1 p.m. on Tuesday, July 21st.",]
     ],
     [
        r"(.*) time (.*) camp duke (.*) end ? ",
        ["Q: What time does Camp Duke end?  A: Checkout will begin at 11 a.m. on Friday, July 24th.",]
     ],
     [
        r"(.*) dress|clothes (.*) camp duke ",
        ["Q: What is the dress for Camp Duke?   A: July is very warm in Oklahoma; please bring comfortable clothing for outdoor activities from morning to evening. Dress is casual, yet appropriate. Refer to the “What To Bring” tab for further details (https://www.swosu.edu/admissions/nso/camp-duke/bring.aspx).",]
     ],
     [
        r"what (.*) registranion fee ",
        ["Q:  What is included in my $200 registration fee? A: All meals, lodging in campus Residence Hall, one official Camp Duke t-shirt (worn on the last day), all activities and events.",]
     ],
    
     [
        r"(.*) camp duke (.*) worth it?",
        ["Q: My summer is really busy, is Camp Duke really worth it?  A: Camp Duke will be an unforgettable experience. Four days and three nights of non-stop fun at Camp Duke will help you feel at ease with SWOSU before you step foot in a classroom. You will meet some of your first SWOSU friends and make memories to last a lifetime! Mark Camp Duke on your calendar right now!",]
     ],
     [
        r"(.*) social|shy (.*) camp duke (.*) me ?",
        ["Q: I’m not a very social person, is Camp Duke really the right environment for me?  A: Camp Duke will help you step out of your reserved shell. Data collected from the last two years of Camp Duke showed that 70 percent of campers wanted to return as Camp Counselors, 80 percent of campers said Camp helped them better prepare for college academically, 98 percent of campers said Camp helped them better prepare for college socially. Camp Duke has something to offer everyone. We guarantee that you will have a great time and meet new people!",]
     ], 
     [
        r"(.*) get to|find|where is (.*) duke",
        ["Q:  How do I get to Camp Duke? A: https://www.swosu.edu/admissions/nso/camp-duke/directions.aspx",]
     ],

     [
        r"(.*)park (.*) duke",
        ["Q: Where can I park? (camp duke)  A: You may park in any of the campus parking lots. ",]
     ],




     

#misc.
    

    [
        r"evert sucks ?",
        ["I agree", "yup.", "totally.", "tell me about it."]
    ],


    [
        r"(.*) (location|city) ?",
        ['weatherford, Oklahoma',]
    ],
   
    [
        r"(.*) (help) ?", 
        ["You may contact the SWOSU helpdesk at 580.774.7070 for additional assistance.",]
    ],
#generic response




    #[
     #   r"(.*)",
      #  ["Q:   A: ",]
     #],

    [
        r"quit",
       ["Thank you"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't catch that, please refrase your question.", "I might not have an answer for that."]
    ],
]
def Carl():
    print("Hi, Please ask your questions here. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    Carl()
