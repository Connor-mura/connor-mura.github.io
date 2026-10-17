# Connor Mura - SNHU CS-499 Computer Science Capstone

## Professional Self-Assessment

---

## Code Review Video
This video is a screen-share walk through and review of my original artifacts before enhancement. This is where I identify flaws, security concerns, and potential enhancements.

* [Watch Code Review Video](https://youtu.be/eze1RcDZMrQ)

---

## Artifact Enhancements and Narratives

### Category 1: Software Design & Engineering
*Artifact Origin: CS-340 Client/Server Development (Python & MongoDB CRUD Utilities)*

The artifact I selected for the Software Design and Engineering enhancement is a database utility class named AnimalShelter that I created in CS-340. This class contains CRUD methods designed to be used with a MongoDB database. The script was originally written in Python and establishes a connection to a MongoDB database instance using a hardcoded MongoClient structure against a collection named animals. This utility was designed to be used by animal shelters to manipulate data records in a NoSQL database and was created to be reusable and portable. In my enhancement, I strove to further this aspect of reusability. 

This artifact was chosen because I believe it represents my ability to build stable backend data interfaces and, through enhancement, also showcases high-quality code generation and clean system design. For my enhancement, this artifact underwent a full Python-to-C++ architectural redesign and was refactored from a hardcoded MongoDB database utility to a fully generic, reusable data management tool. Following Object Oriented Programming principles, I introduced encapsulation to separate memory structure from application behavior by dividing the single utility class into three modular components. Turning the class into a generic template system allows it to support a variety of different record structures, which is a massive improvement on being hardcoded to a single schema. Utilizing predicate wrappers and vector iteration bounds strengthens code stability and maintainability – bringing this program much closer to a production-level system. 

Porting this program from Python to C++ accomplishes multiple goals. The redesign showcases my ability to write clean, functional code in multiple languages and my understanding of the design strength and trade-offs of each. Shifting from an interpreted language to a statically typed language allows type safety to be handled by the compiler, removing the need to use runtime conditionals to verify input data type. The shift away from hardcoded credentials to elastic template definition better aligns with industry standards and best practices while also allowing for a greater tolerance with runtime environment shifts. Porting to C++ does trade off rapid development ease - but increases execution optimization and provides deterministic memory boundaries. 

In order to fully capture the structure of my redesign, let’s look at how the data moves through the program. The Models.h file handles data definitions by establishing strict data schemas. The CrudUtility.h template class acts as an isolated database engine, using internal containers to manage records in volatile memory while using lambdas to run CRUD actions without being married to any one data format. Finally, main.cpp drives the application; setting up test objects and triggering database operations. Now would be a good time to note that my enhanced versions trade off persistent MongoDB database functionality for in-memory data architecture. This shift allows the program to become more lightweight and portable, eliminating external dependencies and increasing execution optimization. I ran some runtime verification tests and documented them in the table below. These tests include verifying that createRecord correctly increments database counts and returns true. Tests also include ensuring that real lookups cleanly isolate matches, that updates correctly modify targets, and that deletes shrink vector bounds without stability leaks. 

| Test Case |	Operation |	Input Scenario |	Expected Outcome	| Results |
| :--- | :--- | :--- | :--- | :--- |
| 1 |	Create |	Adding 3 animal records to the database. |	Database size increases to 3. |	Pass |
| 3 |	Read |	Return all records where breed equals pug. |	Returns animal record A0002 for Lilly the pug. |	Pass |
| 4 |	Update |	Find records where name equals Frank, and change name to equal Air Bud. Return number of modified records. |	Returns 1 modified record. |	Pass |
| 5	| Delete |	Find and delete record whose ID is A0003. Return database size. |	Database size decreases to 2. |	Pass |

The process of enhancing this CRUD utility was a challenging yet rewarding one. I hadn’t yet had the opportunity to work in multiple languages at once – with many courses focusing solely on one programming language. The process of translating functions from one language and design to an entirely different one forced me to become keenly aware of the strengths and limitations of each. This enhancement also forced me to do research and learn more about C++ and the many methods available to developers - which is a skill that only becomes more import as I drift away from coursework and towards real, production-level programming. For me, being able to design something truly reusable was also very rewarding – as this is now a program I can use in my own projects outside of my studies, something that is also important at this stage of my education and development. I believe that programming is a skill itself, beyond the syntax and rules of individual languages, and this artifact enhancement was an excellent opportunity to grow and showcase this skill.  

* [Browse Category 1 Source Files Code Repository](./Category_1_Software_Design/)
 
---

### Category 2: Algorithms & Data Structures
*Artifact Origin: IT-140 Introduction to Scripting (Python Command Line Game)*

The artifact I selected for the Algorithms and Data Structures enhancement is a text-based command line Python game I developed in IT-140. The game takes place in the Fallout universe, a popular post-apocalyptic RPG game, and tasks the player with navigating a maze to collect items. Players need to collect all six items before entering the final room to win. Players navigate using directional text commands like “north” or “west” and can enter “yes” or “no” to pickup found items. The game relied entirely on high-level Python behaviors, dictionaries, and simple loop logic to manage state evaluations. This setup lacked algorithmic depth and custom sorting logic, as it was one of the first projects I ever completed in the Computer Science program - making it an excellent candidate for enhancement.

In order to enhance this artifact, and demonstrate my ability to write custom algorithms, I implemented a custom bubble sorting engine to rank player high scores. This introduces an explicit O(n2) complexity matrix to dynamically organize historic player metrics, in ascending order. I also implemented an optimized, O(logn) binary search routine to cleanly verify, find, and index targeted player metrics. I integrated these search and sorting systems into a structured leaderboard management system which adds a layer of complexity to the game while also adding the element of competition to the player experience. Rather than relying on language specific utility shortcuts, these additions demonstrate my ability to write efficient, optimized from-scratch algorithms. This design also verifies its own logic, as running a search right after sort proves that the data is organized and easy to retrieve. These additions also improve the overall structure of the game while bringing it closer to a production level game you would find in an arcade.

While these additions brought the game closer to production level, it is important to note the trade-offs associated with the chosen algorithms. Bubble sort relies on nested loops that require scanning and swapping records repeatedly. This approach is lightweight and viable for small arrays but introduces scaling bottlenecks as datasets grow. In a larger environment, swapping out bubble sort for a divide-and-conquer algorithm like quick sort or merge sort would optimize processing throughput. Player records are managed dynamically using an in-memory dictionary array. For the purposes of this project, player data is processed in volatile RAM and is lost between game sessions. For this program to ensure data persistence between game sessions, the system would need to pipe the array into an external file or database. In order to verify these additions function properly, I executed search check cases across different sorting scenarios. Testing confirmed that the sorting engine translates unsorted move counts into a clean ascending matrix. Binary search testing demonstrated that searching for active scores reliably returns valid matches while searching for unrecorded scores exhausts index bounds and returns a -1 – demonstrating stability under both successful and unsuccessful searches. The table below documents these test cases.

| Test Case |	Component |	Input Array |	Target Parameter |	Expected Outcome |	Results |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 |	Bubble Sort |	[40, 20, 30] |	n/a | Returns sorted array. |	Pass |
| 2 |	Binary Search |	[20, 30, 40] |	30 |	Target located. |	Pass |
| 3 |	Binary Search |	[20, 30, 40] |	60 |	Search exhausts boundaries. |	Pass |

I found this enhancement to be both challenging and rewarding. I found the process very rewarding for the same reason that I originally chose this artifact for enhancement; going back to one of my very first projects and using my current skills to improve it really showed the journey it’s been throughout my time here at SNHU. The first problem I ran into was sourcing the project – as I no longer have access to the computer I used when I completed this project originally. I needed to reach out to SNHU advising and have them send me the files. This also made debugging and testing my new additions difficult – as I did not have any of my planning documentation for the game, and to test my additions I needed to win the game. Needless to say, I lost many times before I was able to reliably test the program. I am very happy with the outcome for this artifact. This was a pivot from my module one plan, as based on feedback – I realized I needed to switch my planned category two artifact to category one and therefore retrofit my planned enhancement for this artifact for category two – but I am satisfied with the outcome for both artifacts. 

* [Browse Category 2 Source Files Code Repository](./Category_2_Algorithms/)

---

### Category 3: Databases
*Artifact Origin: CS-465 Full Stack Web Development (Travlr Web API Tier)*

The artifact I selected for my category three enhancement, focusing on Databases, is a backend data tier web service I developed in CS-465 Full Stack Web Development. This was originally developed for my full-stack travel application Travlr. The system utilizes an Angular user interface that communicates with a backend Node.js and Express REST API architecture. The model is defined in travlr.js and employs Mongoose to define a schema consisting of key travel data fields; code, name, length, start, resort, perPerson, image, and description. This schema compiles into a Mongoose model named Trip, and operational behaviors are routed via trips.js. Trips.js uses four asynchronous API handlers; tripsList, tripsFindCode, tripsAddTrip, and tripsUpdateTrip. This database interface originally lacked structural validations and defensive code architecture which left the system exposed to data entry issues, incomplete records, and un-sanitized payloads – making it a prime candidate for enhancement.

This artifact was chosen to showcase my ability to build stable backend data tiers, high-quality full-stack code generation, and robust schema validation patterns. My enhancement introduced production level validation boundaries at schema layer. The system ensures data completeness pre-storage by defining required properties and explicit data type requirements inside the model. In order to establish separation of concerns, the application splits duties between the Mongoose data model and controller router layer; the model enforces schema while the router intercepts payloads. As data moves through the system it follows a strict sequence: the payload arrives at the controller layer via req.params or req.body, the controller cleans the input via toUppercase and trim, and then passes it through a whitelist regular expression pattern. If the pattern matches, the data moves to the model. If it fails, the controller short-circuits the pipeline and throws an HTTP 400 error. This process protects the database from bad or unauthorized payloads and preserves backend throughput.

In order to test these additions, I ran verification checks across application endpoints. First, I confirmed that the Node.js Express server starts cleanly from the terminal without crashing. Then I ran validation tests via Postman across add, update, and retrieval operations. This included testing successful lookups alongside malformed payloads – such as a trip code failing the alphanumeric format rule or a price dropping below zero. This confirmed the controller intercepts these variations and throws immediate HTTP 400 errors. I also verified the backend try/catch exception logic by simulating low-level duplicate key collision. The system successfully catches the Mongoose-layer fault and throws an HTTP 500 status instead of allowing a timeout. Finally, I used MongoDB Compass to audit existing records to confirm that legacy data is cleanly formatted to match updated validation parameters. 

I found this enhancement to be a bit easier than my previous two enhancements. One of the difficulties with my previous enhancements was the sheer amount of time between now and the original artifact’s inception. I needed to relearn the programs, relearn the individual working pieces. This artifact was from one of my more recent courses, and all of the program logic was still relatively fresh in my mind. While the process of reviewing my artifact, developing a plan for enhancement, and executing said plan was just as difficult as it has been with the other, eliminating that mental hurtle was huge. The additional tools at my disposal for testing, like Postman and MongoDB Compass, also made the entire process much easier and much more streamlined.

* [Browse Category 3 Source Files Code Repository](./Category_3_Databases/)

---
