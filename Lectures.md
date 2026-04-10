# 🟠 IS508 DA – Big Data and Analytics

## Week 1 Feb 14, 2026

**Data is… – 3Vs**  
**Volume:** The massive amount of data being generated (e.g., 90% of the world's data was created in just the last two years).

**Velocity:** The speed at which data is captured and needs to be used (e.g., real-time fraud detection).

**Variety:** The different formats of data, including **structured** (spreadsheets), **semi-structured** (XML), and **unstructured** (audio, video, social media)

**Data vs. Information vs. Knowledge**  
Understanding the transformation process is critical:

* **Data:** Raw, random, and unorganized ingredients.  
* **Information:** Data that has been cleaned, organized, and processed (transformed via ETL).  
* **Knowledge:** The result of consuming information to make informed business decisions.  
* **Actionable Information:** Information that is specifically useful for business decision-making

**The Five Cs of Data Quality**  
For data to be "whipped into shape" for Business Intelligence (BI), it must meet these five criteria:

1. **Clean:** Free of missing items or invalid entries.  
2. **Consistent:** One version of the truth; no arguments over which number is correct.  
3. **Conformed:** Data uses common, shareable dimensions across the enterprise.  
4. **Current:** Available at the speed required for the specific decision (e.g., up-to-the-minute for fraud).  
5. **Comprehensive:** Contains all the data needed, regardless of source.

Operational Systems vs Data Warehousing

| Feature | Operational Systems (OLTP) | Data Warehousing (OLAP) |
| :---- | :---- | :---- |
| **Purpose** | Day-to-day transaction processing (e.g., bank deposits). | Analysis, reporting, and long-term decision support. |
| **Structure** | Optimized for fast data capture and updates. | Structured for user understanding and complex queries. |
| **Time Horizon** | Current "here and now" data; short time span. | Historical data (past, present, and future trends). |
| **Data Source** | Usually a single source or specific silo. | Integrates many disparate sources into a unified view. |

**Key Analytics Types**

* **Descriptive:** What happened? (Foundational/Core BI) .  
* **Diagnostic:** Why did it happen?.  
* **Predictive:** What is likely to happen next? (Advanced Analytics) .  
* **Prescriptive:** What actions should be taken?.

**Critical Terminology**

* **ETL (Extract, Transform, Load):** The process of moving data from source systems into a data warehouse.  
* **Data Integration:** Combining data from different sources to provide a unified view.  
* **Data Governance:** The process of enforcing rules, definitions, and policies for how an enterprise treats its data.  
* **Self-Service BI:** Tools that allow business users to get their own information without needing IT help for every query.  
* **KPI (Key Performance Indicator):** A measure of performance over time for a specific objective.  
* **Metadata:** "Data about data"—helps users understand what the data means and where it came from.  
* **Operational BI:** Performing queries directly on live operational systems rather than a data warehouse.

**Why Analytics Matters**	

* **Decision Making:** Moves companies from "intuitive hunches" to factual, data-driven decisions.  
* **Performance:** Advanced analytics leaders are twice as likely to be in the top quartile of financial performance.  
* **Competitive Differentiation:** Sophisticated data usage allows businesses to outperform peers.

Extra  
1\. Advanced Terminology & Concepts (The "Nitty-Gritty")  
The second half of the deck contains specific technical terms that are highly likely to appear as multiple-choice or definition questions:

* **Data Preparation vs. Data Franchising:**   
  * **Data Preparation:** The core process of gathering data from sources and transforming/staging it.  
  * **Data Franchising:** Packaging data into BI data stores (like "data marts" or "cubes") so users can understand it. It happens *after* data preparation.  
* **Data Mart:** A subset of a data warehouse oriented to a specific business group (e.g., Marketing) rather than the whole enterprise.  
* **Data Profiling:** Examining source data for anomalies (values, frequency, etc.) early on to prevent problems later.  
* **Metadata:** Defined as "data about the data". It is the enabler that makes decision-support data accessible and understandable to the business.  
* **KPI (Key Performance Indicator):** A dynamic measure of performance over time against a specific objective.

2\. Expanded Analytics & Tool Types  
The slides distinguish between different ways users interact with data:

* **Ad Hoc Query:** Using SQL to ask a specific question when the need arises (the opposite of a routine, predefined report).  
* **OLAP (Online Analytical Processing):** Uses "dimensional models" (often called "cubes") that work like multidimensional pivot tables. It helps answer "what happened and why".  
* **Data Visualization:** Using graphs and charts to help users see patterns they would miss in a standard table.  
* **In-Memory Analytics:** Querying data directly from a system's RAM instead of a hard disk to make analysis much faster.

3\. Strategic Context (Why Businesses Fail/Succeed)

* **The "Shortage" Problem:** A major hurdle for businesses is a shortage of skilled people in BI, analytics, and data integration.  
* **Data Shadow Systems:** These are inconsistent, "uncontrolled" data silos that sprout up when data marts are created without a central strategy.  
* **Governance:** The deck emphasizes **Analytical Governance** (managing reports, dashboards, and spreadsheets) and **Data Governance** (enforcing the rules and definitions of how data is treated).

## Week 2 Feb 21, 2026 Justifying analytics and planning

1\. Historical Perspective: The "Great Split"

* **1995 Database Market Split:** The market divided into two halves: **OLTP** (Online Transactional Processing) for getting data "in" (transactions) and **Data Warehousing/OLAP** for getting data "out" (querying, reporting, and "slicing and dicing").  
* **The 90/10 Rule:** It is generally recognized that **50–90%** of the total technical effort in building a data warehouse is spent on building the data infrastructure, meaning teams usually have more people building data than reporting on it.  
* **Data Hierarchy:**  
  * **Data Mart:** A repository of "like" data (e.g., just Sales data).  
  * **Department Data Warehouse:** A combination of Data Marts for one department.  
  * **Enterprise Data Warehouse (EDW):** A combination of department warehouses to support the entire corporation.

2\. Core Modeling Concepts (Kimball Methodology)

* **Dimensional (Star) Schema:** A **Fact** table (containing quantitative measures) surrounded by **Dimensions** (descriptive attributes like Date, Customer, or Product).  
* **Snowflake Schema:** A variation where a dimension table is further normalized into multiple tables (e.g., a "Date" dimension separating into days, months, and years).  
* **Conformed Dimensions:** A dimension created once for the entire enterprise but used by multiple fact tables. This is the "secret" to decentralized, incremental development.  
* **Slowly Changing Dimensions (SCD):** This occurs when product groups or attributes change over time, requiring a method to maintain a "seamless history" for reporting.  
* **Data Granularity:** Refers to the level of detail (e.g., reporting at a specific product level versus an aggregate product class level).

3\. Business Justification & Sponsorship

* **Why BI Projects Fail:** Most fail due to an **expectations shortfall** rather than technical failure. Flawed expectations lead to projects being late and over budget.  
* **The Business Case:** Must answer what problems are being addressed, who will use it, and what the anticipated benefits are.  
* **The Ideal Sponsor:** Should be a business leader with **budgetary authority** and the ability to secure resource commitments. Projects sponsored *only* by the CIO risk being seen as "technology-driven" and may lack business commitment.  
* **Tangible vs. Intangible Benefits:** A business case should NOT be based solely on intangible benefits like "better decision making." It must focus on **tangible/quantifiable benefits** such as revenue optimization, cost reduction, risk reduction, or regulatory compliance.

4\. Design Constraints & Demanding Realities

* **"Boiling the Ocean":** A common mistake where organizations try to do too much with their first project. The recommended approach is a **BI Road Map** that is a living vision of incremental projects over several years.  
* **Requirement Realities:** Often, the business wants completion in 3 months, while IT estimates it will take a year. A **Change Request Form** is essential to manage shifting requirements.  
* **Assessing Readiness:** You must assess five key areas: Data (the 5 Cs), Expertise/Experience, Analytical Commitment, Organizational Culture, and Financial/Resource Commitment.

5\. The "Bad Decisions" Checklist

* **Unconformed Dimensions:** Having different versions of the same dimension across departments.  
* **Insufficiently Verbose Data:** Not having enough attributes to properly group or constrain data.  
* **Prematurely Aggregated Data:** Losing detail by summarizing data too early.  
* **Lack of Partnership:** A disconnect between IT and business users.

6\. Kimball’s Eight Guidelines for Low-Risk Warehousing

1. Work on the right thing.  
2. Give business users control.  
3. Proceed incrementally (Agile).  
4. Start with lightweight, focused governance.  
5. Build a simple, universal platform.  
6. Integrate using conformed dimensions.  
7. Manage quality a few screens at a time.  
8. Use surrogate keys throughout.

Extra

1\. Expanded Technical Definitions & Models

* **Dimensional (Star) Schema Components:** A **Fact table** (containing quantitative measures like "Quantity Shipped" or "Net Invoice") is surrounded by **Dimension tables** (descriptive attributes like Date, Customer, or Product).  
* **Conformed Dimensions:** These are created **once** across the enterprise but used by **more than one Fact table**. This is the "secret" to decentralized and incremental development.  
* **Snowflake Schema:** A variation where a dimension table is further normalized into multiple related tables (e.g., a "Date" dimension separating into days, months, and years).  
* **Slowly Changing Dimensions (SCD):** This occurs when attributes change over time, such as product groups changing; it requires a strategy to maintain a "seamless history" for reporting.  
* **Data Granularity:** The level of detail in a report (e.g., reporting at a specific product level versus an aggregate product class level).

2\. Strategic Planning & The "Realities"

The deck emphasizes that IT and business often have conflicting "realities" that must be managed:

* **The Time Gap:** Businesses often want a project completed in **3 months**, while IT estimates a quality solution will take **one year**.  
* **Change Request Forms:** Essential for keeping everyone informed of shifting requirements and their impacts.  
* **Technical Effort:** It is generally recognized that **50–90%** of the technical effort in building a data warehouse is spent on the infrastructure (building the data) rather than the reporting.  
* **"Boiling the Ocean":** A warning against trying to do everything at once in the first project. The solution is a **BI Road Map**, which is a "living vision" that evolves over 1–2 years.

3\. Avoiding "Bad Decisions"

The deck lists specific pitfalls that lead to failure:

* **Unconformed Facts:** When the same value (like Net Sales) is calculated differently in different departments (e.g., Finance vs. Marketing).  
* **Insufficiently Verbose Data:** Not having enough descriptive attributes to properly group or filter data.  
* **Prematurely Aggregated Data:** Losing valuable detail by summarizing data too early in the process.  
* **Data Shadow Systems:** Informal, uncontrolled spreadsheets or silos that grow when the main BI system is seen as too slow or expensive.

4\. Detailed Business Justification

* **Expectations Shortfall:** Studies show most BI projects fail due to mismatched expectations, not technical failure.  
* **Tangible Benefits Categories:** Revenue optimization, cost reductions, risk reduction, and regulatory compliance.  
* **CIO as Sole Sponsor:** A major risk; the project may be perceived as "technology-driven" and fail to get business commitment.  
* **Total Cost of Ownership (TCO):** Must include internal costs for both IT and business team members, not just software and hardware.

5\. Assessing Readiness (The 5 Focus Areas)

Before starting, an organization must assess its readiness in:

1. **Data:** (Using the 5 Cs).  
2. **Expertise & Experience:** New architectural and modeling concepts.  
3. **Analytical Commitment:** Moving from "gut feelings" to a data-driven culture.  
4. **Organizational/Cultural Change:** Recognition of the "tectonic shift" required.  
5. **Financial Commitment:** Ensuring resources are actually "freed up" from other work.

## Week 3 Feb 28, 2026 Defining requirements

1\. The Foundation & Common Mistakes

* Defining requirements creates the foundation of a successful business intelligence (BI) solution by documenting exactly what you plan to build.  
* Skipping the requirements phase is not an option.  
* Most BI failures stem from unmet expectations or requirement surprises late in the project, not technology shortcomings.  
* **Common Mistakes in Requirements Definition:**  
  * Requirements are not detailed enough to set expectations.  
  * Focusing *only* on business requirements while ignoring data, technical, or functional needs.  
  * Failing to refine and update requirements as the project inevitably changes.  
  * Excluding business power users or BI designers and developers from the process.  
  * Simply re-creating the existing legacy system along with all its current warts and inefficiencies.

2\. Goals & Required Documentation

* **Primary Goal:** To define the requirements needed to design, build, and implement BI solutions within an agreed-upon timeline and budget.  
* **Deliverables:** A finalized set of requirements agreed upon by business sponsors, stakeholders, and IT management, plus a revised project plan with updated budgets and resource commitments.  
* **What the Requirements Document MUST Include:**  
  * Project description, functionality (key deliverables), and assumptions/dependencies.  
  * Authors, contributors, and list of interviewees.  
  * Inputs used: databases examined, source system documentation, and existing data shadow systems.  
  * Requirement priorities and issues/concerns (budget, scope, schedule).  
  * Change management tracking (additions/modifications) and formal sign-offs.

3\. The Five Categories of Requirements

A complete BI solution must document requirements across five distinct areas:

1. **Business Requirements:** High-level needs, supported business processes, business rules, and metrics/KPIs.  
2. **BI Functional Requirements:** Specific use cases documenting the "why, where, and how" users do their jobs. This also includes process workflows, user interaction, and analytical styles. Functional requirements should not just be generic statements like "drill down into data details".  
3. **Data Requirements:** Identifying the Systems of Record (SOR) – the authoritative data sources. This requires drilling down into specific columns/fields and defining rules for data conformance, integration, and quality.  
4. **Regulatory & Compliance Requirements:** Industry or country-specific laws, such as Sarbanes-Oxley (SOX) for 7-year financial data retention, Basel for banking risk, or PCI for payment card security.  
5. **Technical Requirements:** Infrastructure standards (e.g., cloud vs. on-premise), vendor hardware/software rules, web services, and database access policies.

4\. Roles and Responsibilities

* **Business Analyst (BA):** Takes the lead on defining requirements. The BA must be able to communicate with executives and IT, understand business models, and be "data savvy" enough to explore data sources deeply.  
* **IT Roles:** Data architects, data modelers, ETL designers, and BI designers. These roles usually skip initial business interviews but join later to define detailed data and functional requirements. IT also provides Subject Matter Experts (SMEs) for source systems and infrastructure.  
* **Business Roles:** Sponsors, stakeholders, and users who have a vested interest in the solution.

5\. Data Profiling & Quality (The Reality Check)

* **Data Profiling:** Must be performed early to check for data anomalies, identify unanticipated business rules, and discover PK-FK (Primary Key-Foreign Key) relationships.  
* **The "Go/No Go" Decision:** Profiling provides a fundamental baseline to decide if the project can even proceed.  
* **Gap Analysis:** Compares the requested data requirements against actual source data quality. Gaps must be fixed via ETL processes, MDM (Master Data Management), new source identification, or dropping the requirement entirely.  
* **Data Quality Myths (Do not fall for these):** Problems do *not* originate in the data warehouse (blame data silos instead). Source data is *not* always excellent (it's often inconsistent or old). Data cleansing tools will *not* magically fix all quality issues.

6\. Methodology: Gathering & Prioritizing

* **Top-Down vs. Bottom-Up:**  
  * *Bottom-up:* Gather new requirements to ensure vital features from existing systems are not lost.  
  * *Top-down:* Determine existing requirements by engaging stakeholders to ensure they have their say and to validate via feedback loops.  
* **Prioritization:** Requirements must be classified as: *Must-have, Should-have, Nice-to-have,* or *Forget about it*.

7\. Organizing Around Business Processes & The Bus Matrix

* **Processes \> Departments:** Design the BI solution around business processes (e.g., a "Companywide Sales Data Mart") rather than creating siloed departmental solutions (e.g., "Marketing Dept Data Mart").  
* **Strategic Initiatives vs. Processes:** Strategic initiatives are org-wide, 12-to-18-month plans with financial goals. Business processes are the low-level activities (billing, shipping) that generate the actual metrics used for analysis.  
* **The Enterprise Data Warehouse Bus Matrix:** A master map of the organization's data strategy.  
  * **Rows:** Represent the core business processes and strategic initiatives.  
  * **Columns:** Represent common dimensions. These are discovered during interviews by listening for "by" and "where" phrases (e.g., analyzing sales *by* date, *by* customer).

8\. The "Do's and Don'ts" of Interviewing

* **DO:**   
  * Talk to a vertical span of people (executives down to analysts).  
  * Use a two-person team with one designated lead interviewer.  
  * Ask open-ended questions like "what do you do and why", "how", and "what if".  
  * Flesh out your scribbled notes *immediately* after the interview.  
  * Conduct sessions face-to-face (or voice-to-voice).  
* **DON'T:**   
  * Rely on a single user just because it is easier.  
  * Schedule more than 4 interviews per day.  
  * Ask "what do you want in the data warehouse" or show them a list of data elements.  
  * Accept static, generic requirements documents from the business.  
  * Rely on non-interactive surveys or assume a 3-inch binder of legacy reports equals requirements analysis.

Extra

1\. The Prioritization Quadrants (Highly Testable)

On slide 55, there is a critical matrix used for prioritizing projects based on **Business Benefit** (High/Low) and **Feasibility** (High/Low). four zones:

* **High Benefit / High Feasibility:** *Initial Sweet Spot Zone* (Do these first\!).  
* **High Benefit / Low Feasibility:** *Pre-Work Required Zone* (Needs more foundational work before starting).  
* **Low Benefit / High Feasibility:** *IT Comfort Zone* (Easy for IT to do, but doesn't offer much value to the business).  
* **Low Benefit / Low Feasibility:** *Career Limiting Move Zone* (Avoid these completely).

2\. Specific Techniques for Documenting Requirements

The deck lists specific tools you should use to gather and document different types of requirements:

* **For Business & Functional Requirements:** Use storyboards, BI mock-ups, and prototyping of BI objects.  
* **For Data Requirements:** Use data profiling and the output from data modeling, ETL, and BI tools.  
* **For Current State Reporting:** Use sample reports, sample spreadsheets, and sample data.

3\. The "Stepwise Refinement" Process

Slide 14 outlines a specific visual flow for defining requirements. 

1. It starts with defining **Business Requirements**.  
2. This branches out into four parallel tracks: **Data Requirements**, **Functional Requirements**, **Technical Requirements**, and **Regulatory & Compliance Requirements**.  
3. All of these ultimately merge to form the final **BI Requirements**.

4\. "Wrapping Up" Challenges (Discussion Points)

Slide 56 highlights specific real-world challenges you face when finalizing requirements.

* **Budget Silos:** Historically, senior executives paid for projects strictly from their own departmental budgets. Moving to a BI model requires asking them to look at funding from a shared, *enterprise* perspective.  
* **Resourcing:** Getting actual time commitments from team members is incredibly difficult because everyone is already fully committed to their day jobs.

5\. The Highly Specific "Don'ts" of Interviewing

Interview rules \+ very specific warnings that might pop up as true/false questions:

* **The "Latte" Rule:** Don't bring food to the interview or spill a large latte over the interviewee's conference table and sample reports.  
* **The Inquisition:** Don't overwhelm a lone interviewee by having six IT people sitting across from them "Inquisition-style".  
* **Analysis Paralysis:** Don't allow the requirements-gathering phase to be overcome by "analysis paralysis" or the pursuit of process perfection.

## Week 4 Mar 6, 2026 

1\. The Four Pillars of BI Architecture

A proper architectural framework prevents "accidental architecture" (chaotic data silos) and allows your BI solutions to evolve and expand over time. It consists of four parts:

* **Information Architecture:** Defines the "what, who, where, and why". It outlines the business processes being supported, the users involved, where the data currently lives, and the overall business requirements.  
* **Data Architecture:** Defines the schemas, data integration, transformations, and storage methods. It covers the data's journey from creation in source systems all the way to analytical consumption.  
* **Technical Architecture:** Defines the underlying technologies (e.g., cloud platforms, in-memory analytics, massively parallel processing) needed across the whole BI life cycle.  Sources\[...\] → Integration → Warehouse & BI data → BI \+ BI portfolio\[...\]  
* **Product Architecture:** Defines the specific vendor products, configurations, and interconnections used to implement the technical architecture.

2\. The Evolution of Data Warehousing (SOR, SOI, SOA)

The industry has shifted away from using a single, monolithic Enterprise Data Warehouse (EDW) toward a broader "data warehousing" ecosystem containing multiple data stores.

* **SOR (System of Record):** Operational systems (like CRM or ERP applications) where data is captured and updated. They are designed for transaction processing, not for reporting or analytics.  
* **SOI (System of Integration):** Gathers, integrates, and transforms data from the SORs into a clean, consistent, and conformed state.  
* **SOA (System of Analytics):** Provides this newly integrated and transformed information to the BI applications so business users can analyze it.

3\. The Data Integration Framework (DIF)

Data integration is a combination of architecture, processes, standards, people, and tools. A common pitfall is oversimplifying data integration by equating it purely with an ETL (Extract, Transform, Load) tool.

The DIF is split into two major processing stages:

* **Stage 1: Data Preparation:** The heavy lifting. This involves gathering, reformatting, consolidating, transforming, cleansing, and storing the data. This stage can consume 50% to 90% of the total project effort.  
* **Stage 2: Data Franchising:** This takes place after preparation. It involves filtering, reorganizing, transforming, summarizing / aggregating and storing the data from the data warehouse into "franchised" structures like ***data marts*** or ***OLAP cubes***. The goal is to package the data so BI tools can effectively present it to users.

|  | Preparation | Franchizing |
| :---- | :---- | :---- |
| Sources | Many conflicting src | DW or ODS |
| Is data clean? | no | yes |
| Are dimensions managed | no (SCDs, conform, etc) | yes |
| Data storage | mess | RDBs, documented DMarts |

Two roles of BI in the information architecture are to provide:

* Back-end processes that select, retrieve, and transform the data stored in the information architecture.  
* Front-end processes visible to BI application users to interact with, analyze, and present results in graphic or tabular form.

4\. Highly Testable Sub-Concepts

* **Metadata Management:** The classic definition is "data about data".  
  * *Technical Metadata:* Used by software tools (not people) to understand data formatting, mappings, and table structures.  
  * *Business Metadata:* Explains the business context, where the data came from, and what it means to the users analyzing it.  
* **Accidental Architecture:** The chaotic result of building tactical projects without a long-term plan or just chasing vendor hype. Symptoms include having multiple scattered BI tools, relying on unmanaged "data shadow systems" (like messy spreadsheets), and thinking new technologies will act as magic bullets.  
* **Data Cleansing vs. Data Quality:** Data cleansing tools are specialized software used for complex matching (like standardizing variations of a customer's name and address). However, these tools are not a "silver bullet" – you must build data quality processes into the entire architecture, not just rely on a tool.

Extra  
1\. The 6 Exact Steps of Data Preparation

Data Preparation is the "heavy lifting," → six explicit steps:

1. **Gather and Extract:** Getting data out of custom, on-premise, cloud, or external source systems. *Best practice:* Make the group that maintains the source system responsible for the extraction process.  
2. **Reformat:** Converting source data into a common format and schema.  
3. **Consolidate and Validate:** Standardizing multiple sources into a single definition and validating data against dimensions/reference files to ensure referential integrity.  
4. **Transform:** Applying business rules, algorithms, and filters to turn data into a business context (e.g., associating a transaction with a specific product hierarchy).  
5. **Cleanse:** Performing complex analysis beyond basic record checking, such as name-and-address cleansing or customer householding.  
6. **Store:** Saving the data to make it available for further processing.

2\. Data Franchising Design Considerations

When packaging data for Business Intelligence (BI) tools to consume, there are specific dimensional schema designs to consider:

* Star versus snowflake schemas.  
* Pre-built aggregated tables.  
* Handling hierarchies.  
* Shrunken dimensions.  
* Slowly changing dimensions vs. rapidly changing dimensions.  
* Multi-valued dimensions.

3\. Alternative Data Store Technologies

Relational databases dominate BI, but alternative technologies are growing. The deck explicitly lists the following alternatives to replace relational databases in certain architectures:

* OLAP databases.  
* Massively parallel processing (MPP) databases.  
* Data virtualization.  
* In-database analytics and In-memory analytics.  
* Cloud-based BI, DW, or data integration.  
* NoSQL databases.

4\. The Architecture Action Plans

If you get a question asking what is required to execute each architectural phase, here are the explicit summaries:

* **Data Action Plan:** Define needed data, examine source system completeness/correctness, identify facts and dimensions, define logical data models, and establish a preliminary aggregation plan.  
* **Information Action Plan:** Define the transformation framework, recommend data stages, develop source-to-target mapping, review data quality procedures, and define physical data models.  
* **Technology Action Plan:** Define technical functionality, review overlapping technologies, assess current strategic tech directions, and recommend technologies.  
* **Product Action Plan:** List product categories, review trade-offs, outline stage implementations, identify a short list of products, and make final recommendations.

5\. The House Analogy & Security

* **The House Blueprint:** The deck compares building a BI environment to building a house. You start with the purpose (Information Architecture), make a wish list, and hire an architect to tell you what is practical given your budget and constraints.  
* **Security & Privacy:** With massive amounts of data flowing, security and privacy must be *foremost* in the architectural framework to avoid catastrophic breaches (like those seen in retail, healthcare, and finance) and to comply with government regulations.

## 

## Week 5 Mar 13, 2026

1\. Data Architecture Fundamentals

Before diving into specific systems, you need to understand what data architecture actually is and why it matters.

* Data architecture acts as a blueprint that aligns a company's data with its overarching business strategies.  
* It defines the data, schemas, integration, transformations, storage, and workflows needed to support analytical requirements.  
* The primary goal is to ensure data is available, accurate, clean, current, comprehensive, and consistent for business decision-making.  
* **Benefits:** It helps you understand your data, guides data management from capture to consumption, provides a structure for data governance, enforces security/privacy, and supports Business Intelligence (BI) and Big Data activities.

Data Architecture vs. Data Modeling  
Do not confuse these two concepts\!

* **Data Architecture:** The high-level view of how an enterprise categorizes, integrates, and stores its data. Think of this as the architectural blueprint for an entire house.  
* **Data Modeling:** The highly specific, detailed rules about how pieces of data are arranged within a database. Think of this as the specific instructions for installing a single faucet.

---

2\. The Evolution of Enterprise Data Warehouses (EDW)

* The early 1990s marked the dawn of data warehousing, heavily evangelized by Bill Inmon, who is often called the "Father of Data Warehousing".  
* The goal was to centralize data to create a "single version of the truth" for an enterprise view of the business.  
* At the time, they were called Central (or Corporate) Data Warehouses (CDWs), but today they are typically called Enterprise Data Warehouses (EDWs).

**Inmon's 4 Classic Attributes of a Data Warehouse:**

1. **Integrated:** Data is gathered and made consistent from one or more source systems.  
2. **Subject-oriented:** Data is organized by business subject, not by the application that generated it.  
3. **Time-variant:** Historical data is strictly maintained and stored.  
4. **Non-volatile:** Data is read-only; it does not get modified once in the DW.

---

3\. The Rise (and Fall) of Data Marts

* Data marts emerged as a backlash to the large, slow, and cumbersome CDW projects.  
* They were quicker and cheaper to build because their scope was strictly limited to a single business group, rather than the whole enterprise.  
* **The Trade-off:** To save time and money, builders skipped the hard work of standardizing data definitions across the enterprise, which severely limited data breadth, integration, and quality.  
* **The "Data Silo" Problem:** While initially successful, data marts eventually caused chaos. Different departments would show up to meetings with conflicting reports, debating whose data mart had the "right" numbers.  
* **Types of Data Marts:**  
  * *Independent Data Mart:* Extracts data directly from the source systems, completely bypassing a central DW.  
  * *Dependent Data Mart:* Part of a hub-and-spoke architecture where it pulls its data directly from the central DW.

---

4\. Alternative Data Structures: ODS and Federated DWs

**Operational Data Store (ODS)**

* An ODS is designed to bring data together from multiple sources in near real-time to enable operational reporting or specific business processing.  
* **How it differs from a DW:** An ODS loads data as-is without extensive transformation/cleansing, focuses on current data without maintaining history, and is organized around application-specific processes rather than business subjects.  
* **Best Practice:** Use the ODS as the System of Record (SOR) feeding into the EDW.

**Federated Data Warehouses**

* This architecture splits a single EDW into multiple physical DWs.  
* Splits can be based on geography/countries, business functions (e.g., HR, sales), or business entities (e.g., subsidiaries).  
* **Best Practice:** Design the EDW logically as a single data store, but implement it physically as federated based on business/performance needs.  
* **Limitations:** Federated DWs often suffer from performance issues, lack of data integration, and lack a reliable source of historical data.

---

5\. The "Accidental Architecture" Problem

* Because companies built quick-fix solutions over time, the current reality for many enterprises is an "accidental architecture" full of overlapping and redundant DWs, ODSs, data marts, and shadow systems.  
* For example, Sales and Finance might build entirely independent DWs without synchronizing their data.  
* Because these isolated silos were built for parochial departmental interests rather than the whole company, they end up causing more harm than good from an enterprise perspective.

---

6\. Major Architecture Choices & The Recommendation

Major architectural choices an enterprise can make:

* EDW-only.  
* Independent data marts.  
* Ralph Kimball's enterprise data bus architecture.  
* Bill Inmon's Corporate Information Factory (CIF).  
* Hub-and-spoke.  
* Analytical Data Architecture (ADA).

**The Recommended Approach:**

* The slides strongly recommend the **Analytical Data Architecture (ADA)** using a **hybrid dimensional-normalized model**.  
* This approach is flexible and accommodates various data stores, including hub-and-spoke, systems of integration, and systems of analytics.

Extra  
This covers the specific definitions, secondary points, and organizational context that weren't in the initial summary.

1\. Granular Definitions & Comparisons

* **The "System of Record" (SOR) Role:** The slides emphasize that an ODS should be the **System of Record** for the Data Warehouse. This means the DW shouldn't pull from everywhere; it should pull from the ODS, which has already consolidated the operational data.  
* **Data Architecture vs. Information Architecture:** While I mentioned Data Architecture, the slides define it as the layer that "enables the **analytical requirements of the information architecture**." Data architecture is the technical "how," while Information architecture is the "what" the business needs.  
* **Integration vs. Transformation:** The slides explicitly list "schemas, integration, transformations, storage, and workflow" as the five components a data architecture must define.

2\. The "Why" Behind the Evolution

* **The Failure of Early Apps:** A key point skipped was *why* we needed DWs in the first place. Early transactional applications were "siloed" and only kept **limited current data online**. If you wanted to see what happened three years ago, the app often didn't have it. The DW was the solution to this "amnesia."  
* **The Data Mart Backlash:** Data marts didn't just appear; they were a **rebellion** against the CDW (Corporate Data Warehouse). CDWs were seen as "too big, too expensive, and taking too long."  
* **BI Tool Influence:** The slides note that the "explosion of BI tools" in the mid-to-late 90s is what actually forced companies to build data marts, because the tools needed a structured place to "plug into."

3\. Detailed Architecture Specifics

* **The Hybrid Model Recommendation:** The slides don't just recommend the Analytical Data Architecture (ADA); they specifically recommend a **"hybrid dimensional-normalized model."**   
  * *Normalized:* Good for data consistency and reducing redundancy (Inmon style).  
  * *Dimensional:* Good for user speed and ease of reporting (Kimball style).  
* **Federated DW Types:** The slides mention that federated warehouses can be split by **Geography** (countries), **Business Function** (HR, Sales), or **Business Entity** (Subsidiaries).  
* ![Federated Data Warehouse Architecture, AI generated][image1]

4\. The Risks of "Accidental Architecture"

* **Shadow Systems:** The slides warn about "data shadow systems"—these are the manual spreadsheets and "under-the-desk" databases that employees create because the official DW is too slow or difficult to use.  
* **Parochial Interests:** A specific term used in the slides is that silos are built for **"parochial interests"** (narrow, departmental focus) rather than the enterprise's health.  
* **The "Harm" Factor:** The slides make a strong claim: solutions built without an overarching architecture inevitably **"produce more harm than good"** when looked at from an enterprise perspective.

5\. Technical Architecture Components

* **System of Integration (SOI):** The slides identify this as the layer where data is cleansed and combined.  
* **System of Analytics (SOA):** This is the layer where data is formatted for the end-user (usually dimensional).  
* **Unstructured Data:** The slides mention that a modern ODS can be used for **"refining unstructured data"** before it moves into the warehouse.

If you see a question about "The Hub and Spoke" model, remember it is the middle ground \- it has a central warehouse (the Hub) that feeds departmental data marts (the Spokes). This is often the "gold standard" mentioned in Inmon-style architectures.

To hit the **80/20 Pareto Principle** for this course, you need to stop looking at the individual slides and start looking at the **Data Lifecycle**.

---

1\. The Core Transformation (The "Why")  
Everything in this course is about moving from **OLTP** to **OLAP**.

* **OLTP (Operational):** Fast, messy, "here and now." Optimized for *inserting* data (e.g., a bank transaction).  
* **OLAP (Analytical):** Historical, cleaned, "big picture." Optimized for *querying* data (e.g., "What were our sales in Q3?").  
* **The Goal:** Moving from **Data** (raw ingredients) → **Information** (cleaned/ETL) → **Knowledge** (business decisions).

---

2\. The Architecture (The "How")  
If you are asked about architecture, remember the **System of Record (SOR)** to **System of Analytics (SOA)** flow.

* **Stage 1: Data Preparation (The 90% Effort):** You Extract, Transform, and Load (ETL). You must hit the **5Cs** (Clean, Consistent, Conformed, Current, Comprehensive).  
* **Stage 2: Data Franchising:** You package the data into **Data Marts** (department-specific) or **Cubes** so business users can actually understand it.  
* **The Architecture Pillars:**   
  * **Information:** The "What/Why" (Business needs).  
  * **Data:** The "Schema" (Star/Snowflake).  
  * **Technical:** The "Tech" (Cloud, In-memory, MPP).  
  * **Product:** The "Brand" (Snowflake, AWS, Oracle).

---

3\. The Kimball Methodology (The "Structure")  
This is the most technical part of your exam. If you see a question about "modeling," it’s almost always about the **Star Schema**.

![Star Schema vs Snowflake Schema diagram, AI generated][image2]

* **Fact Tables:** The "Numbers." Quantitative metrics (Price, Quantity, Temperature).  
* **Dimension Tables:** The "Context." Descriptive attributes (Date, Customer, Product).  
* **Conformed Dimensions:** **This is the most important term in the course.** It means using the *exact same* Dimension table (e.g., a "Master Calendar") for multiple Fact tables. This prevents "Accidental Architecture" and data silos.  
* **SCD (Slowly Changing Dimensions):** How you handle history when a customer moves or a product category changes.

---

4\. Requirements & Strategy (The "Business")  
Why do BI projects fail? **Expectations Shortfall.** 

* [**The Bus Matrix:**](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/kimball-data-warehouse-bus-architecture/) A technical "map" where **Rows** \= Business Processes and **Columns** \= Conformed Dimensions. It’s the blueprint for the entire company's data.  
* **The Prioritization Matrix:**   
  * **High Benefit / High Feasibility:** Your "Sweet Spot" (Do this first).  
  * **Low Benefit / Low Feasibility:** "Career Limiting Move" (Avoid).  
* **Governance:** Enforcing the rules. Without it, you get **Data Shadow Systems** (uncontrolled, rogue spreadsheets that everyone uses because the official DW is too hard to use).

---

5\. Summary Checklist for the Exam  
If you can explain these 5 things, you will likely pass:

1. **The 3Vs:** Volume, Velocity, Variety (The nature of Big Data).  
2. **ETL vs. Data Franchising:** The "Heavy Lifting" vs. the "Packaging."  
3. **Star vs. Snowflake:** Star is simple/fast; Snowflake is normalized/complex.  
4. **Independent vs. Dependent Data Marts:** Independent \= Siloed chaos; Dependent \= Pulls from a central EDW (Best practice).  
5. **The "Accidental Architecture":** The mess created when you build "Point-to-Point" integrations instead of a centralized strategy.

---

---

MIDTERM

## Week 6 Mar 20, 2026

1\. The Analytics Framework

Data-driven decision-making requires the right data, tools, skilled analysts, and a supportive environment. When analysts, domain experts, and tool experts combine their efforts, they generate useful insights.

Analytics is divided into four main ascendancy stages based on value and difficulty:

* **Descriptive Analytics:** Answers "What happened?" using historical data aggregation and data mining. Example: Wal-Mart identifying that young males buying diapers on Fridays also tend to buy beer.  
* **Diagnostic Analytics:** Answers "Why did it happen?".  
* **Predictive Analytics:** Answers "What will/could happen?" using statistical models and forecasting. Example: Forecasting increased diaper demand in summer due to expected birth rates.  
* **Prescriptive Analytics:** Answers "What should we do?" or "How can we make it happen?" using optimization and simulation algorithms. Example: Determining the exact dates and discount percentages to maximize both sales and profit.

---

2\. Descriptive Analytics (DA) in Practice

Descriptive analytics collects, organizes, and presents historical data easily.

* **Functions:** Evaluates current performance, historical trends, and business strengths/weaknesses.  
* **Advantages:** High objectivity, useful for identifying new variables, and flexible enough for both qualitative and quantitative data.  
* **Disadvantages:** Only reports the past, relies on simple analyses (usually 2-3 variables), and may suffer from a lack of truthfulness in the underlying data.  
* **Core Execution Steps:** State business metrics $\\rightarrow$ Identify required data $\\rightarrow$ Extract/prepare data $\\rightarrow$ Analyze data $\\rightarrow$ Present data.

**Pareto Analysis:** Based on the "80–20 rule" named after Vilfredo Pareto, this analysis identifies the "vital few" by sorting data and calculating cumulative percentages. For example, 80% of sales often come from 20% of customers.

---

3\. Data Queries & Excel Functions

**Essential Excel Functions:**

* **Calculations:** SUM (adds numbers), AVERAGE, MIN, MAX, COUNT (counts non-empty cells).  
* **Logic & Lookup:** IF (conditional statements), VLOOKUP (vertical search), HLOOKUP (horizontal search).  
* **Frequencies:** COUNTIF(range, criteria) counts cells meeting a condition. FREQUENCY(data\_array, bins\_array) groups values into intervals.

**Data Filtering & Summarization:**

* **Sorting:** Arranging data in ascending or descending order.  
* **Auto Filter:** Retrieves specific rows and hides others based on simple criteria.  
* **Advanced Filter:** Performs complex filtering across multiple columns simultaneously.  
* **PivotTables:** Quickly creates custom summaries, cross-tabulations, and allows you to drill down into large datasets by dragging field names.

---

4\. Data Visualization (Charts)

Good visualization allows users to compare data, control scale, map back to details, and filter subsets.

* **Column & Bar Charts:** Compare individual items. Bar charts use a vertical axis for categories and a horizontal axis for values.  
* **Line Charts:** Show continuous data trends over time on an evenly scaled axis.  
* **Pie & Doughnut Charts:** Show parts of a whole (percentages). Doughnut charts can display more than one data series.  
* **XY (Scatter) & Bubble Charts:** Plot functional relationships; Bubble charts add a third variable represented by the size of the bubble.  
* **Area Charts:** Plot change over time and show part-to-whole relationships by summing the plotted values.  
* **Radar Charts:** Compare the aggregate values of several distinct data series.  
* **Surface Charts:** Find optimum combinations between two sets of numeric data, using colors to indicate ranges like a topographic map.  
* **Stock Charts:** Show fluctuations in specific ordered data, like prices, rainfall, or temperature.

---

5\. Statistical Methods

Statistics extracts information from data through estimation (point estimates for a single value, and interval estimates for a range).

A. Measures of Central Tendency (Positional & Arithmetic)

* **Mean:** The arithmetic average.  
* **Median:** The middle value when sorted. Half the data is below, half is above. If $n$ is even, it is the mean of the two middle numbers.  
* **Mode:** The most frequent observation.

B. Measures of Position

* **Percentiles:** Calculated by sorting data and finding rank $= \frac{nk}{100} \ 0.5$ (where $n$ is observations, $k$ is percentile). Use PERCENTILE(array, k) in Excel.  
* **Quartiles:** Divide data into four parts ($Q1$ \= 25th, $Q2$ \= 50th, $Q3$ \= 75th). Computed using QUARTILE.INC(array, quart).  
* **Cross-Tabulation (Contingency Table):** A tabular method displaying observations for sub-categories of two categorical variables.

C. Measures of Dispersion (Spread)

* **Range:** The numerical difference between the greatest and smallest value.  
* **Variance:** The average of the squared deviations from the mean. The larger the variance, the greater the expected variability.  
* **Standard Deviation:** The square root of the variance.  
* **Coefficient of Variation (CV):** Relative dispersion calculated as $\\frac{Standard Deviation}{Mean}$. Its reciprocal is known as "return to risk".

D. Measures of Shape

* **Skewness:** Measures the lack of symmetry.  
  * *Positive Skew:* Tails to the right.  
  * *Negative Skew:* Tails to the left.  
  * *Coefficient of Skewness (CS):* $< -1$ or $> 1$ indicates high skewness. Values between $0.5$ and $1$ (or $-0.5$ and $-1$) indicate moderate skewness. Values between $-0.5$ and $0.5$ indicate relative symmetry.  
* **Kurtosis (CK):** Measures peakedness or flatness.  
  * $CK < 3$: Flatter with wide dispersion.  
  * $CK > 3$: More peaked with less dispersion.

---

6\. Sampling & Probability

* **Sampling:** Selecting a subset to estimate characteristics of the whole population.  
* **Probability:** The likelihood (from 0 to 1\) of an outcome occurring in an experiment. The complete collection of possible outcomes is the sample space.  
* **Event Rules:** \* *Mutually Exclusive:* No common outcomes.  
  * *Joint Probability:* Intersection of two events.  
  * *Conditional Probability:* Probability of Event A occurring, given Event B is true. Events are independent if $P(A|B) = P(A)$.  
* **Random Variables:** Can be discrete (counted) or continuous (real numbers over an interval). Their probability distribution characterizes the possible values and their respective probabilities.

## Week 7 Mar 27, 2026 (raw latex, refine)

1\. Descriptive Statistics Recap

Before predicting the future, you must quantify the present using central tendency and variability metrics.

* **Central Tendency:** Includes the Mean ($\\sum\_{i=1}^{n}x\_{i}/n$) , the Median (the middle reading when data is sorted) , and the Mode (the most frequent reading).  
* **Variability:** Measured using Variance ($\\frac{\\sum\_{i=1}^{n}(x\_{i}-\\overline{x})^{2}}{n}$) , Standard Deviation (the square root of variance) , the Coefficient of Variation ($SD/mean$) , Range, and Inter-quartile range.  
* **The Normal Distribution:** In a normal curve, 68% of the area lies within $\\pm1\\sigma$, 95% lies within $\\pm2\\sigma$, and 99.7% lies within $\\pm3\\sigma$ of the mean.  
* **Standardization:** Quantities are converted to a standard normal distribution $N(0, 1)$ using Z-scores: $Z = (x - \mu)/\sigma$.

---

2\. Inferential Statistics & Sampling

Predictive analytics relies on taking uncertain data samples and inferring population statistics (like estimated means and standard deviations).

* **Why Sample?** We use samples instead of entire populations due to cost, practicality (scale), and to avoid bias.  
* **The Central Limit Theorem (CLT):** As the sample size increases ($n \\ge 30$), the distribution of the sample mean approaches a normal distribution $N(\\mu, \\sigma/\\sqrt{n})$.  
* **Standard Error (Known Population $\\sigma$):** Quantifies sampling error using the formula $SE = \sigma/\sqrt{n}$.  
* **Standard Error (Unknown Population $\\sigma$):** Estimated using the sample standard deviation ($s$) with the formula $SE \\approx s/\\sqrt{n}$.  
* **Confidence Intervals:** For large samples, a 95% confidence interval defines a range where we are 95% certain the true value lies, calculated as $\\bar{x} \\pm 1.96 \\cdot SE$. Critical Z-values are 1.64 for 90% confidence and 2.58 for 99% confidence.  
* **Small Samples (t-Distribution):** For samples smaller than 30 with unknown standard deviations, use the t-distribution, which has thicker tails and depends on degrees of freedom ($n-1$). The confidence interval becomes $\\bar{x} \\pm t \\cdot s/\\sqrt{n}$.

---

3\. Hypothesis Testing (A/B Testing)

Hypothesis testing provides a formal framework to prove or disprove business claims.

* **The Hypotheses:** The Null Hypothesis ($H\_0$) is the default claim, which is given the "benefit of the doubt" until statistical evidence from a sample rejects it. The Alternative Hypothesis ($H\_a$) is accepted if the null hypothesis is rejected.  
* **Significance Level ($\\alpha$):** A 5% significance level corresponds to a 95% confidence level.  
* **T-Statistic:** Measures the distance of the sample mean from the claimed mean in units of Standard Errors.  
* **P-Value:** The probability of seeing a sample with at least as much evidence in favor of the alternative hypothesis as currently observed, representing the risk of mistakenly rejecting the null hypothesis.  
* **Rejection Rules:** You reject the null hypothesis if the claim falls outside the confidence interval, if the absolute t-statistic exceeds the critical value, or if the p-value is less than your significance level (e.g., 5%).  
* **Interpreting P-Values:** A p-value $\> 0.05$ does not prove there is no true effect; it means the observed data is not surprising and should be treated as noise.  
* **A/B and A/A Testing:** A/B testing randomly assigns users to different designs to measure performance differences. A/A testing (placebo testing) is used to understand platform baselines and identify when a test might yield a false positive.

---

4\. Correlation vs. Causation

* **Covariance & Correlation:** Covariance measures how two variables co-vary. Correlation is a standardized version of covariance that ranges from **\-1** (perfect negative correlation) to **\+1** (perfect positive correlation).  
* **Zero Correlation:** A correlation of **0** means there is no *linear* relationship, though points may still form a non-linear pattern.  
* **The Golden Rule:** Correlation does not imply causation. Two variables may move together purely by chance or due to an unmeasured third factor (spurious correlation).

---

5\. Simple and Multiple Linear Regression

Regression models the actual numerical relationship between variables for forecasting and control.

* **Simple Linear Regression:** Uses the equation $y = a + b \cdot x + error$, where $a$ is the intercept and $b$ is the slope (the increase in $Y$ per unit increase in $X$).  
* **Ordinary Least Squares (OLS):** The mathematical method used to find the best-fitting line by ensuring the mean of residuals is zero and the standard deviation of residuals is minimized.  
* **Model Quality ($R^2$):** $R^2$ represents the proportion of variation in the dependent variable that is explained by the regression model.  
* **Multiple Regression:** Expands the model to include several independent variables ($Y = a + b_1X_1 + b_2X_2 + \dots + b_nX_n + error$).  
* **Adjusted $R^2$:** When evaluating multiple regression, always use Adjusted $R^2$. It compensates for the number of variables and data points, allowing you to fairly compare models with different numbers of predictors.  
* **Variable Significance:** To ensure an explanatory variable actually matters, check that its confidence interval does not contain zero, its absolute t-stat is > 2, and its p-value is < 5\%.  
* **The Danger of Multi-collinearity:** This occurs when two or more explanatory variables are highly correlated with *each other*. It confuses the software, leading to unreliable coefficient estimates, large standard errors, and artificially small t-stats. Always check scatter plots and correlation matrices before running a regression to drop redundant variables.  
* **Forecasting Warning:** When using your regression equation to forecast future outcomes, be extremely careful about extrapolation (predicting data points far outside the range of your historical sample).

[image1]: <data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/2wBDAQMDAwQDBAgEBAgQCwkLEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBD/wAARCAFMAdYDASIAAhEBAxEB/8QAHQABAAICAwEBAAAAAAAAAAAAAAYHBQgBAwQCCf/EAGQQAAEDAwIEAQUGDBAKBwgDAAECAwQABQYHEQgSITETFBUiQVEWFzJhgZYjN0JSV3F2kbTR09QYJDM2VVZYYnJzdZOUsbXSCSc4Q1NndKGkwyU0Y2Sio7MmREZlZoKywYWSlf/EABkBAQEAAwEAAAAAAAAAAAAAAAAEAQIDBf/EAD8RAQABAgIDCwsCBgIDAAAAAAABAgMEERIhMRQzQVFScXKRkrHREzI0U2GBobLBwtIV4QUiNZOi8HOzIySC/9oADAMBAAIRAxEAPwD9U6UpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKV886Ckq5hsO53rgutJbLqnEhA6lW/T79B90rhKkrSFpUClQ3BHYiuaBSleeTcIEJxhmZNYYclL8NhDjgSXV7b8qQfhHb1Cg9FKUoFKUoFKUoFK6ZcuLAivTpshtiPHbU6664oJQ2hI3Uok9AAATvXmsl9suS2tm949dolyt8nmLMqK8l1pzYlJ5VJJB2IIPxg0HvpSvh55qO0t99xKG20la1KOwSkDck0H3SsTiuWY1nFgi5TiF7iXe0TucxpsRwONO8i1IVyqHfZSVA/GDXlj6gYTKveQY4xlFuVcsVajv3uMXgFW9t9Clsqe36ICkIUoE+pJoJBSuqLKjTozM2G+2/HfQl1p1tQUlaFDcKBHcEHfeu2gUr5WtDSFOOLShCAVKUo7AAdyTXisl+smS29N1x+6xbjCWpSEyIzocbUUnZQCh0OxBFB76UpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQac/4QGBMyTL9BsC90l5tFtynLn7dcV2qauM64yY4O3On46imqWmWT8D96wbVDSrU/NLzjNwyWFYslxy/Xbyth9iUvw0OtqUklLiVqHt6dRtt1srjf011kzK76RZlo1greVz8EyZy8SoS7ixDBb8IJA53lpHUjbpuajF8024q+KnLMQja5YBj+nGA4pe2b5Kt0a8idPuj7I3aQS0S2lsL2O5UDuOxoJXqlxc6qYzmWUWDTHhrk5XZ8MCUXS83XJ49hQ89yFa24jUhsqkhKQPTQdiTsB1SVVjqhxTavZpmnDLm2imnE+5WXOEXS4Jsz+SM29N0kJhuJXEeJQoJDACnkuKBC+gCUnth9VOFrWjKdWtSpmR6GWLVEZXNXIxDJb7k5agY1GKCER1wvhkoPXdtJBJG5PqzcXh04ksF0n4b52GYlj9zzDRl65puNom3UNMyEy2Vs8yHUjYgJWVEbg9uh7UE/wBW+LzWPDchzJGEcOrNzxrBBvOut/yZuyuXHlQVOeRMOtFTqE7EBwEhW3QHdO+wul2e27VjTPGdSLZBfiQsqtEW6sxpBBcabfaSsIVy9NwFbHatFdSeDbW7KM/1Rk3bSvCs/m5jcJUrGcyyG+vJ8wQXQoIiCKEqIW0lQCSkcpKQonc7DcvhuwjJtNdBsE08zFqI3eMascW1S/JHi6ypTCA3zJUUpJBCQew232oNI7xqfkmjvD7xIaF+epE/KIeXnHMYZfUsS5Ea+uJS2po78xUEuS1t7H/MCsHMyfO8J4UtQuEObkM24ZnbtQ4GB2y5vTCFiNcX23oz3MDz7BAPP7PEI9VbE6s8H2TZ9xl4XrZAnwGsHhv2+8ZLDXKWmTIutsbki3ONoCCkpSp1AO6x0K+h6V953wY3fKuN/FeJSJdbc1jNtiJeuttWVeLIuDKFoYcDYTyK6OcxWVApLadgaDF6qcRmuGlEu/4vppp7gtjw3TC3xI3nLPLvJhOX5CY6SW7akJAVycim+dalBSgCD1APznHGhrDdbHoGvQvS+wXO+64Wy5S0QrzNcDVucjMR3Ny4jl5kIDril9ASlvYbE1Ds74KNc7jrBqfl0Oy6YZnHz2Y65ar/AJY9KcuGPxXEKT5OzHSgtFLYXyo9L6hJ6Hep3pXwp6s4jc+GObkEzHCnReDktvvfk0x1ZkImxUMRVMbtDmPobrCuXl36FVBHdQONzWC0ZwnR6yr0VxjL8ctEeZllwzO/vx7V5a6NxDghsh1agBuVK3A32PqJr3VfifyXXvCOHvVbTjEoicvjajyrM7Znp5XCTcm4q0H9MNj6Ixs4h3mSD6O4BJG5uTVjhT1Jg67X7WzRzGNMMrTmMNhi72bOozim40hnomRHcQ2tQKgdlJ2A6DvXzauD3VCDjmkLFyy/H7hecRzd/Lr+4xCTBipS8yUGPEaabAKUeikFexOxO46AB9Y7xg6rac5PqngHE5heM+fNPcRTnEaThjz6oc+3bhCm9pRDiXA4pKdyADsvpskFeKVxV8UumEPAdUuIHA9OIWmufXaFa1IscyYq62MTAVR3pJcBZcSlIJXyb7+rYkAz3UjhNuOp2vWeZ1ebzFYxbNtLjgjjbKleVtSVS/FLu23LyBAHXfffpt66hLnClxHamw8E0r12zzEJenGn11h3QO2mM8Llf/JElMdqQlfoMJAJCuUq3B9RAICdY/xL5vdrbxIS5NnsqHNHVy02UIbd2khq3qkp8o3cPNupIB5OTp8fWqu1M429TrPieh0mDMwjCjqhirV/uuTZFElOWqFJUw0vyZsNKJRupw+k6rYJ5epO5EhznhT4hEZfq1G0n1HxO2YjrKC5ePOdvdemwFmN5OtLISQlYWjcbkjl5twDtWVu/C1rLadPdMMawfULG5pwbGo1guthyK1eV2a7KaaShL/hndTbidiQevTagjGXcbWpWD8N+L5rkUDT1nNswylOMW65MXlMnHPBPOrzmpxlxawyG0jdBUFhStyNhsczwx8V2W5trTM0NzPNsFz7xLIq+W3JsQCm2dkOIQ7GkNKUoJWC4kpKe6QSaw8D/B3yGtEBhT2d2yNmLOdHUGDPjWdPmyDO8MNiMiIpR3jciRugnqrr26VZmhXDtqThepkvVLU7N8cmyTavNMK043Ym7bCZQVhS3VgbqW4SkbHpsCR1oI5/hHdUYmE6FM4Ichj2WXqRdY2Nie+vkRDiOLBlPlW4CQhsE9SARuPXVb8A+qWH4blWrnC3g+cWrJbBir7mT4RPgyTJYXbpKErfjJXuQfAeWjcb7qW68ewrYXPeGxnU3iFxrVvN7nbbtjOKWeRDgY1KtwdQZjx9OStSlFKtkhISnk6devWsVqJwkWO8atafau6WSLNg1xxFUyLc2YVobS3d7fJQErYWG+QBQ9LlWd9udXTtsGveCcVHFLa9B814tdQsixe7YjaWJtntGNRLZ4Mg3UXFmFFfecAB8IuOLLiUr+CAQNz6NwYjB42bDdbS/qblOL53ieWWeUq+R4ttYtb2LvFhS0JaUFlU1vc+GTtzevYAbnOYbwdWW38Ld94ZM3yHzvAvsq4SVz4rBYUyt+WZLK0JKlek04G1Dc7EoHTbpXiwHhh1oj5bjd61h4hnsqteEw3otit1vtnm4OKWyWfEmqDivKVBv2gDm60GpHDrm/ExopweacazWTVKwLwRGSeZmsOcx5DjjsZ+8vMOuuTSsOJc8VTpCUjYJCPS3JFWjrzeMkyKRxt2Gx3O3WXzRhmMzRLatDK5EmMq2yXZDDrnRa+dtKm0LUSWuclI6bG2bfwUyofCLjPDA5nzS3sevKLsbuIJCXeW6OTuTwufcfqnJvzerf4qlVx4U4V7yLW+63XK3vJNZ8ftlgfYZYCVwERITsYrSokhZUHSrqBttt1oNW8q4ktT9DMA0N0ZuWtbNnfyrHkX24ZknDDOct1sSyExoTMFgr8VYUAhTqgCRsroQQfqw/4QLP8AHdMdXWXsj93lxxNuGvEsrkYs7Z254lFLe0iK5y8qmnFEDpsoJ3O4OwvBvgqy9OIYLITrdLY1J01L0fH8qYtqEoNvUOVMKRHJIdaCOh6gkknpWdtfBtGv2CZ9j2tWpV8za86joSm6XBSjHZhcgHhiFH3KGQkpSfWTt1PWgiz+C8YNihlq+cRNmyawZRi1zN1cmWONClWqd5OFMOQW0FQfSSopKF7JASo9SpPLR3DvnOqGkvCtoJIs2drdYzLWO045Jjrt7KQxa33X0vxgrYk86mubnOyhvsDtWy+GcIN6bzixZnrDrPe8/wDcdAlW3G4kiM1GbjIfQG1vO+GPorxQAOboOgO24rBReAG0R9JnNJDq/lPkNryljLcVloSyl+wTWlrUnwiE7LH0Rz4QPfcdRQeXVrXHUvHOILVHBrPkamLRYdI5eSW2OGUHwbihp5SXuYjc7FKeh3HTtVLNas8UGl3CVbuJTK9dJeQ3vUqLa4FttfmNtxix+UPJQmS0lKh4r3gDco5QFOKO+52NbD4zwRMwclynOM21myvLciy/FZeJz5k5uOgIivIKAWkoQOUoCjsDuNz13qbSuFfArpw42jhrvk+5TbLZIEaHDuPOG5jTscgsyEqSAA4lQBGw26UGt/Dnq/q1bOInE8AiZRqvmmF5ZAuHnuRnuNGC5bJzLPitvRXgkbtLUnw/CPRHNuSolPLvxWv2mXCS3hupVp1UznWPM9Q73jkB632I3x1pLVubeTyPKQhpKQpS0bAlW/atgaBSlKBSlKBSlKBSlQ3V7PTplp9ds4UljwrS15Q+p5JUlDQ6qVyggqO3YAjc7UEypVMr1Z1rNvYnW/h/lTQ+kKSXbzHjbpI3Ctm/HIG23x1zH1g1hbdKb1oQIraRzKVGusyUdviCLfsT8QNBctKpG5cU9lx+baIWUaaZ7bE3m5xLQzMesT7UREmQ6lpsKdfS10KljsCdgSAdqu6gUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgVSvGbClXHhkzy3wklT0qC1HSPbzyGkn/AHE1dVQ3WOFFnaXZM3NSCwzb3JS9wD0Z2d9YP1lBIcdKVY/bSj4PkjO32uQVkah2jd6GSaTYdkAVzC5WOFKB33352Uq7/LUxoNduNaFMuOL6YxIfN11Uxlx3b/RtyFOK3+L0K2Jqq+JIQoenCspuAHhYvMbvIJ2HKtpCwk7kHb0lirRaVztoX9ckGg+6UpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKVHc9v03G8ZlXe3TrNFfYTzJXdnlNR/tFSeu/sA7mtQZuteuWpN/axiw3N1D8t1TbMe2NeEFJPrKiObkA68yuw6ms5MZt05l6tFvdQxNucZl11aW0NrdAUpSjskAd+pqP6uwJt10ozS121pbsuZj1xjx0IG6lOLjOJSAPWSSKjGkGiMXAkpyDI5qrxkzzfK5LeWXBHB7obKuu3tPc/aq1Kwy1O0s1U1d020qwvTyFot5e9i2NwLfcZN1ucq1JceZZQ2ox3nYRhPA7bp5paCexCT2xX6JPWK53lVvvGW4Fi1lnqlMJel8tru8BbL3hqU0pLl1hywCDsSGwrlPwav3iB0sOrum8rGYt4ZtVxjvs3G2y5DSXWG5bKwtvxm1dHGyRyqSe4JrXS3s6pWKbGjYtqZp9jORyZKot9sOEYq5kbMp1CSrkW6Et+b9wTsHlIbBUTv3oJXeuE7UzWayyLdq1xjZdkOMXFk+SxsatECzJfZX1HlKkpebkjblIIbR1G42radtAabS2CSEJCQT36Vrnpu7qnhGMnHcSs8VmK/INzY91M/xX4/jkqMMMwkKZjshYUAsSHfD5+qFbBNXlhWXWrOsZhZRZl/QJYWlbRcQtcd9tam3mFltSkeI06hxtYSpQCkKAJ23oM5SlKBSlKBSlKBSlKBXw660yguPOobQkblSlAAD7Zr7qmbpilh1Q1wvNkz61Rb5ZsXtMJ2BbJrfjRA/IKyt5bKt0LXsgJBUk7DfaqcNYpvTVNc5U0xnOUZztiNUZxwzHC43rk24iKYzmZyj/AH3LZ89Wb9loX8+j8dPPVm/ZaF/Po/HVRZHhHC1iWSR8dyPSLT+3+NaJd6XMkY9Bbjsx47rDSytZRsn0pLff46wqDwTP5BjuOwsI0xlvZRHuUm3vsWGCuOpEENmSFucmyCkOpOx7gK9lddHBcqvsx+TTPEcVPXPgvfz1Zv2Whfz6Px089Wb9loX8+j8dUo3buCJ2AxdG8e0fVFkzBb2XRa7fs5JJADQ9DcqPMk7ewg9utINu4IbnEuE+3WDR2THtTbbsxxq225SWUL+ASQjsT0G3r6d+lNHBcqvsx+RniOKnrnwXX56s37LQv59H46eerN+y0L+fR+OqUx+w8JmWZnCw3GNJtProu42FzIo02Jj0FyM5GRJEdQCwj4YcOxHq2IPUbVOf0Pmgv2EsC+bcP8nTRwXKr7MfkZ4jip658EyF6s5IAu0Mk/8Abp/HXsBB6g71Af0Pmgv2EsC+bcP8nWL0rx6JgWf5pp7jq3GMbjRrZebbbSoqaty5RlJfaY3J5GiqMHA2NkpU4vlAB2pNjD3Ldddmqc6YzymIjVnEbYmdeuODj18aLt2iumm5EZTq1T7Jni9i06UpUKkpSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApXClBIKlEADqSfVVe3zV+Cq4OY7gNseym8oPKtEU7Ro5O/V174KftDc0E+lSo0KO7LmSG2GGUFxx1xYShCQNyok9AAOu9VtM1WuuVyHbTpHYzeFIUWnbxI3bt7Cux2UerpHsT07ddjvXyzpTeM0kNXPWC9m6NoWHWrFEUpq3MqG+xWB1eUN+6jt37g7VZUSHEt8VqFBjNR47CAhpppAQhCR2CUjoAPYKCAWfSGPLuDeQ6j3dzKLsg87aH08sKMe+zTHwenXqrc7d+1Z7F9PMaxS73fILdCSbnepC35MlY3WEqVuGkn6lA6dB32G/YbSelApWtea646tWewZ/q7Z1YyjENOp8tmRZJMZ3y+5RoaQqU4iR4gQ05sSW0eGoKIAJHN0kV+4tcDxmy3C/3q1XNmHbbnfLW8sJSol22EJWQAeocUQE/b67UEZ15tr1n1XiZNmVsm3/GL5CbssK3LcddtqJHpKCXo6d0lxayQFKQoKBATyrbSlz12eBqtlMODFsGJt2W2NuQ3G3JbRaDbI5udKUuhKyUbJHVls7dOoJFc2vjItmRQoDWM6Y5Bdb5Ou79pTamXmUqCm4XlvipdUQhaCzv8E9FpUnuKsLS/XPHtWlTxi1smpbttthzJLsgBCGpD6Vq8kUd+jiEoQpXqAcTQRy2cOBubSPfEy2VeBsguQ0gLjqKXS5spDoLagTt18MLB6hW/WrZxnGbLh9mZsGPxVx4MdTi0IW+48rmcWpayVuKUpRKlKPUnvWrOIcV+pFpl3O56qWeIIsK0TL1ItEK1PMPsRWXUkvRJSnFsXBpMdXiKWjwzsnok7ip3kXGJhtkvke2Rcbuc6FKvsqxR7oHG2Yj7sYsNvltxwhKil55xoJ3BUqM9tuB1C/6Vq7K43YGLwvCzTA5yLu9dsgaYgwpDbqjbbZMEdUjffYrKlpQGx1UpKyOm1ZG88aECDcJMW0aTZNdoyU3FcOU26w0mWIMZuTI2StQUjZp0bcwG6vR70GyNKxmM5Bbssxu1ZVaFLVBvMJi4RStPKosuthaCR6jyqHSsnQKUpQKUpQKrDFfp/53/JFo/wCdVn1WGK/T/wA7/ki0f86rsHvd7ofdSmxHnW+l9JefWDRF3VK7ouSb61CbFgl2RTTkbxQrx5kORzn0h0AhlPL6+fffpsawy/gsl5Hkd0u0HOYdviXp7KGZLCbWrnZiXmLEaV4C0up5HWlwkKCiCFB1Y2SQCbsm5beGNb7RgqHWxapmLXG7Oo5BzGQzLhtIPN3A5X3Onxj2VStx4/8ATS05jf8AGJdiluNWsXduE5Fmx3ZU2RbW1OSG1RuYKjpWlt3wXFq2X4Z5/CJQFwqXZpnwc3LEcwx/M8lzC3XORZbs7cVRm2Jz6HUmAYiB4k6XIcChvz9Dyj4IHTevIvgtvNuwHFsVxfPoMCZjuPRrHIfTb3WRcPDlIfUpS2HkPM83IRzNr50k7g9wfTknGxLxKBeI+R6TJtWQWOYqHJt8/K4DDKymKmQrwXlHmeUoOIQhCGiSsnm5E7KObg8Ws3JrPIy7AtGcgvmNQ7XGnSZy58SM809ItzdwbY8nKypWzDzQUpJVs4sJSFDdQD16D8M1z0fyS25HccxYuzkKy3e1ONtRn0Bap15XcfEC333nTy+J4fprWpW3MVkmr8qA6Tav2TWJm+3XFY/i2S0zmbfHuSXgtue6YrL7xb2HwW1Phknf9UbdGw5es+oFQDH/AKeGa/c/YP8A1rlU/qv7CpKNbs1UtQSBj1g6k7D9WuVW4Xer3Rj56E1/z7fS+2pYFKd6VEpKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUqM5hqLieDspN7uX6ae6R4MdJdkyFdPRQ2nqe469B1G5FBJqhWV6sY1jUvzNDRJvl7X0btdtR4z5P77bogfGojsaj6YOqup48S6vO4LjrnaGyoLukpBH+cX8FgfvRurYqB9Rqb4pg2L4VE8kx21NR+bq48fTedPtWs+ko/bNBCRhGf6kLEjUy7eZrMTunHrS+QpweyTIGxX/AAUbDt2NWJZLBZMbgN2uw2uNAitjZLTDYSn7fTufjrIUoFKUoFKUoKX1I4QNB9VbtKvuVY1ckzpb/ljjlvvk6E2ZYSEiSWGXUsqdASn01IJPKObcDashO4WdDrpfLtf7jiMiS9e/LTMjOXeaqGpctKUyXERfF8FtxzkSStCEq5hzb83WrYpQVtjHD9pnhUiPdcZtEpN3hTXrnGn3G6TZ7wluQxD53FvPKW6kMBLYQpXKAPR5T1ru0a0hgaT45dLYp23TLhf7rKvF1kQrd5Ew9IfVuQhkrcKEJSAlIK1HYdzVh0oKkhcNuBYlDlu6cwEQLl5DJgWxF6lT7va7czIVu801AclJbbaUOhbaLY22HYbVj7Pwi6PQ9PMN08vFrm3CLh1uTAbcYuMqCmcStDr7khph1KHfFfR4ykrChzE+01ddKCpb1wsaJ38um4Y5cx40q4Sl+T3+4R/+vLbXLZHhvp2jurZbWpgfQuYc3LuSTmfeD0nCkFGKJbDYuAQhuW+hCBOZQzJSEhYACm2kJAA2Ty+jynerBpQY/H7Fa8WsNtxmxxjHttoiMwYbJcUstsNICEJ5lEqVslIG5JJ9ZNZClKBSlKBSlKBVYYr9P/O/5HtH/Oqz6rDFfp/53/I9o/51XYPe73Q+6lNiPOt9L6SzmcaRYDqHc4N6yq1SXp9tYdjRpMa4SYjiGnFIUtHMw4glJU2g7HfqkVF8g4YNKLtDvyrbYhAud7gzoaZqnXZAiqloKX3mmXFltK17nmUACrcgn0jvU3Gtjyb9kGPuzrMZ8aBZriuM1OsMq6W96SpbOwR5MFLjTAlJ8J8oIAUvbY1homp3EBHyCDpZa2LtbJTmLx89QuUw3Okwbc1BcjOWxwcqS68q4pjr3+Eppx0Agp6QqVlYHwXaX45bri3lnleRXG6znp0mYZciMforSGnGgUO85bUhpAUlSjvyips1w76XWd6LdMTxmNabraoLEO1vpW6tmMqOwGIzhYK/DcW22EoClAq5QBvWpNm1C4lrvDxnInn8zu13sTl98jbdtKmYt0nm1hcNl5IYaPhKkboCloRyFRTzn4RzGAaj8U2ZW+04/JyfJ4rVyusBuVefc6G5UVLsR5chGzsZLaUpdbb23Qrk5uUrWSDQbbaNaV2LRXTWy6a46tTsS0NL5nlpCVPvOOKdedIHQFbi1q2HQc2wqa1o1ddQ+KezYKqU/kuSLmXWw4rfXZBxwBcCTLcuSZ0Nnw2F+GEiNE38Rt1SC76WwWCnbTR++37JdMcbvuURprF2mQG3JaJkYMPhzsStsdEk7b7D29h2oJjVYGxw8l1V1BsU8uBibjVhaWW1lKk7vXLqCOxB2NWfUAx/6d+a/c/YP/WuVW4Xer3Rj56E1/z7fS+2p5NP8mvdgvZ0tz2QHLm02pyz3A9E3SKnvt/2qB8JPfbr261ZVRfUHBLfntlEJ51cSfEcEm3T2ejsSQnqlaT7N+49Y+PYjG6cZzLvK5WJZWhEXKLMAmW12EhHZL7ftSr4uxqJSnVKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKV47rd7XY4LtyvE9iHFZHMt15YSkfKf6qD2Vh8oy/GsLtpu2UXmNbowOyVPL2U4r61CR6S1fEkE1Bl6i5dnq1Q9KrFyQSSlV/ubZbj7b92W/hO9NiD0H3tqyuM6R2W13NGT5NLfyXIRsRPuOywwd99mW/gtAHqNhuPb1oMQm/6malbJxa3O4jYXNv+k7g1+nX0e1pk/ABHZSviOxqS4dphi2HOKuEaO5OuzoHj3OcsvSXTtt8JXwR8Q26dKl1KBSlKBSlKBSlKBSlKBXjvN0j2S0Tr1LQ4tiBGclOpaTzLKEJKiEj1nYdBXsrz3CK3OgyIToBRIaW0oH2KBB/roKBHHJovGuEi2X2UzY5MNxTMlm5ZRjrTrDiSQpDjYuRcQoEbFJSFA9CK9Uvjs4U7e2lc3WGzBS+zcRSp6j9ryUOg/JvXp4Kb2/knDxZ79J+HcLzkMgdfqVXmaU/7tqvOgpHHONDhvy2am34/nsuVIUoISgY9c0bk9huqOB1q5oE+FdYMe522S3JiS2kPsPNq5kONqAUlST6wQQQfjqI60y41o0jzW+vMoV5rsE+4DdIPpMsLcB+QoFYvhmnv3Thv0puckkvTMJsb7hPcqXAZUd/lNBZVKUoFKUoFKUoFKUoFVdi7iEcQmcMLVyuO2W0uISe6kgvAke0A9KtGohmml+OZtNjXiU/c7Zd4bamY9ztU1yJKQ2oglHOgjmTuN+VW4qvCXbdvTouTlFUZZxry1xOzVxOF+iqrRqo2xOfwmPql3fvWLg4pjNsv9zyq3WC3xrzekMN3G4NR0JkS0MpKWkuuAcywgKUEgnYbnbuagPvDf64NS/nE5+KnvDf64NS/nE5+Kt/IYX1v+M+LXyt/wBX8f2WnSqs94b/AFwal/OJz8VPeG/1wal/OJz8VPIYX1v+M+J5W/6v4/stOlVZ7w3+uDUv5xOfip7w3+uDUv5xOfip5DC+t/xnxPK3/V/H9lp1XeMSo8nXHPER3kuKjWPH2Xgk78jnPcF8p9h5VoO3sUD668A0H2O51f1LPxe6N38VTHCcBxrT+3yYGOxXUqnSVzJsmQ8t+RLfV8Jx11ZKlq22A3PQAAbAAVtnh7Fq5TRXNU1REbMsv5onPb7Mve1yu3a6ZqpyiJz258Ex9UiqD6kYNNvoi5TibzcPK7IS7AfV0Q+n6qO77W19viPUEdanFK89Wi2n+dxM5tCpCoi7fdIa/J7lbnT9EiPj4ST7R6wfWKlNVtqFi95st2RqhgjXPdYiAm528dE3OKO6f4xI6pPyVMsVye0ZjYouQWSQHYspO49SkKHRSFD1KSdwQexFBl6UpQKVDrjm1yuE9+yYDZm7vLjLLUqY+8WYENY7pW4AVLcH+jbST9cUbg18pwjJLqQ7leoFye3O5i2lAt0dP2igqfPyukH2Cpd06c5WaZq9uyOudvuzcPL6Wq3Gfd1+GaXPSY8ZBckPttIT3UtQSB8prFrzPEG1crmVWdJHqM5oH/8AKsUzpRgLRDj2PMy3d9y9LWt9xR9pUskn5ay7OI4rHQG2sbtiUj1eSI/FWc8TPBTHvmfpBnfngiOufpDr922Gftts39Pa/vV7oV6s9y3823WHL27+A+lf9RroOL4yRscdtm3+yN/irHTNN8Dnq5pWJ21R9oYCf6tqx/7McmeuPE/88cU9ceKSAg9RXNQ06ZW6GAcbyG/WNSTugRZynGk/EGXudr/w10uXLUTENnLxEj5VaUD6JKt7Pk9wZH1yo5JQ96iS2pB9jZpOIrt77RlHHGuPpPwJvVUb5Tq441/v8E4pXis94tt+t7N1tMpEiK+N0OJ9ftBHcEHoQeor21TTVFcRVTOcS7RMVRnBSlKyyUpXBISCSQAOpJoOa635DEVlciS8hpptJUta1BKUgdySe1QTJNXrVBnrxzD7dIynIOwhwCC2yfa88fRbHt7nt09dY6NpjkuauIuer1+ElsKC27BbVKbgNd9g4r4Tx6+vYdx6QoO64atyr7LdsmlViVkM1BKHJzhLdvjHqN1OfV7H6lPfbbcVzatITdZ7eRaqXpeUXRB52Yqk8luhn2NMdlbduZe5PTcb9asC3W232mI3AtcJmLGaHKhplASlI+ICvTQfLbbbSEttIShCRsEpGwAr6pSgUpSgUpSgUpSgUpSgUriodmOr2neCNqOQ5NFbeA3EZo+K+rvtshO59Xc9PjoJlSq2051Pvmqc5dzseMrteLx1FPls87yJi/rW20+igA91FSvYADuRZNBS3CDZW8W0PtmIpAC7JLmRnQN+jinlPKB39e7tXTWpuiuv2J4BK1Vtebs3uIlnUi+ogOt2eS5FXEaU0ylXlIR4KPojTqfTWnYpPq61I5vGVCn3RnGcM0uvsy8zvDNvNxfbTb5gc8Uo2lW4Tg3zCO/t4iED6GrtsaC1dd7a9etD9Q7PHG7s7FbtGQPapcR1I/3mudDLa1Y9F8FsDPwbPj1vthHXoqOwhpQ69ehQRVS3rKONbP7OmPh+k+neJpkByPcGMrvC57DrKhylUaRAWVEkE9HY6NvXv2q4dIMaybEcAgWDMHYK7qxInOumE+p9lKHZbzrSQ4ptsqIbWgE8ifSB2G3WgmVKUoFKUoFKUoFKUoFKVXmWajZO3ksnCtOcPbv13gxm5M12VL8liRQ4TyIUvlJUtQBISB0A612sWK8RVo0cGuc5iIiPbM6nO5dptRnV4rDpVR+6fia+xZiHzhX+Sp7p+Jr7FmIfOFf5Kqv025y6O3T4uO66eTV2Z8FuUqo/dPxNfYsxD5wr/JU90/E19izEPnCv8lT9Nucujt0+Juunk1dmfBblKqP3T8TX2LMQ+cK/yVPdPxNfYsxD5wr/ACVP025y6O3T4m66eTV2Z8FuUqpW8n4lg4nxdK8SKNxzcuQr329e30Kpdp7nrecQ7iiTaX7Rd7JNVb7pbX1pWuM9yJcSQpPRSFtuIWlXTcK9oIrndwNy1RNedMxG3KqJy58p+LajE0V1aOUxM8cTHellKUqNQVU2T2yTpFf5GouNxnnceuCwrIrayNw0e3ljSfUR9WB3HX1VbNeK8Inu2uS3bGozslTag23J38JZ27K267Gg6YGSWO5mCIFyZf8AOUZcuLyHcOsp5ApY+IFxHfr1+I175CVrjuobc5FqQoJVtvynboa0SvWTZ3phqdb7hcbM7ZxaJC3ottDhXHDDiiHUNKPdCgVD4t/VtW8FkvdvySxxL7ang7EnMJfaUCOxHY7diOxHqIIpVGpjbCEaDZXZL5pzYrfCQqJPg22KJsN9Phvc620q8fY9VodJLiXBuFcx3PMFAWRVbYJhtgyfSnBnrlFUiXFx6B5NNjuFmSxvGb35HE7KAPTdPwTt1BrLJsOo1nVtaMth3VgcwS1d43K4kerd1rbmP/2ivMwdy9aw9uK6dKMo1xzcMT9M+aNiLDV3KLNEVU5xlGuObhjwz9yZ0qG+6XUOGkKuGniJCUnZa4NzQpSvjShaU/eJrtGeXHb0tOMrB9YDMY/86qd12+HOP/mrwd90UcOfVPgltKiRzy4fY4yz+Yjflq6zmeVy1hu1aaXUHuVT5LEZI+0UqXv96s7rte3s1eBui37eqfBMa886fBtkR2dcZbMaMwkrddeWEIQkdySegFRXm1VuwIDVjsLSlbbqUuY8ge3pyoNfUXTe3yJTVxy65zMklsrDjaZpAitLB3BRHT6G4O2xVzEbDYiseXuV6rVE886o6tvw955WurzKffOr9/gwek1988ZRnPkcFyLbFz402ClxBQpaXWEhTgQfgpWpouAbAnnJPU1ZlQjFB/jLzr/+MH/DmpvWmApmmzo1TnMTV80tcJE02spnPXV80lKjuX5/iuDR0O3+5pbeeO0eI0PEkSFb7ANtj0lHfp7KhwOq2piQdl4PYHBv6l3OQggfIz6/32x9RFWqUhzLVXF8QlIsxW/db7IH6Xs9tbL8pw7b9Up+ANuu6tugO2+1R4YnqPqMfGzy5qxuzq7WW2P7vrT7HpA/qR0+P1VMMP0/xXBo7jWP2xKHn+siW6fEkSD7XHD6SuvyfFUjoMVjmLY9iVvTa8ctEaBGT9QyjbmPtUe5PU96ytKqm8ZrneX6m3TTbTqTb7SxizMSRfbtOjmQrnkpUtqOw0CAo8iSpS1HYeiADudtqadJThsNViZqymIimM5mdkRnEe2dsxGqJnOVq7j203HtqCe5XVn7K8H5uo/K09yurP2V4PzdR+Vpoxx97puW16+nqr/BO9x7abj21BPcrqz9leD83Uflae5XVn7K8H5uo/K00Y4+83La9fT1V/gne49tNx7agnuV1Z+yvB+bqPytPcrqz9leD83UflaaMcfebltevp6q/wAE73HtpuPbUE9yurP2V4PzdR+Vp7ldWfsrwfm6j8rTRjj7zctr19PVX+CeUqocsv8AqvpZ5LlF8vtqybGxIYjXJtMDyOTFS66lAeQQtSVhJUN0nr7KtxC0uIS4k7hQBH2qTTlGbTEYSqxRTciqKqas8pjPbGWca4ic4zjg4X1SvDer3acctj95vlwYhQoyeZ155YSlI/8A2SegHckgCq2Vfs61ZUuNiCX8axhfMhd4fb5ZctJHeOg/BSfUs+o9K1SuzV7KbNPbOn1oN1uuRywfDgWeSWls7p3C5Dg6NI6g+kRuPi61r3pdw7X7Ls3uEfKgW7VZJi4859Cyryl5J6tNqI3V8avV9s1tvh2CY1gsBUKwQA2t9XiSZLiud+S561uOHqok7n2bk7Ab1nWmGWApLDKGwpSlkISBuonck7esk7k1nNjJ0222wbPAYtdsitxosZAbaabTslKR2AFemlKwyheU6Z2efZsgXhsK3Y1k15ivobv0GC0iW1IWDs6XAnmUeY7nfffrWqcTE9YX7tjtz1J4arzkF1tTyE3O7Lz2M1BXIjpdbZmrYeKFOI5XnHUpQs8pWdxvvV88RmaZ1hhxmRYLkLZjkuU6xfprTQXLQlQQllMYkKSl0lSyOZKuYoCAOZQqtLtecXfuHgOWS6ZjdoqYdyYcvCXnZKHg+GG5bcNaVOR1BKnCVpiobO6Vc3Teg40R1JzvFL/lKrnb7Nk2M3NTcuwW/ARJnx23FOFLvNOkckFrfoS0JPRQVsK2SwnNLdnFqenw2H4kmDLdt9wgSQkSIUps7KacSCQNwUrSd9ltuNuJJStJNQMYzrllbDkFuJAxqBs+yhTraEupSHQEcqfonKC2CR0Ke3QVY2m2mHuBm3y8zMluF6ud/caVJfkuucgQ1zhsJbUtSUK2cIUUcqVbA8o2oJ1SlKBSlKBSlKBSlKBVYac/Td1Q/wBotf4OqrPqsNOfpu6o/wC0Wv8AB1Vdhd5v9GPnpTXt8t88/LKvtaNctScC1InQLfcLPbsStka1l2a9Y3rigSX3nQ8iW+zISYKQ2GSgqaWDz83avbfOMTGsWkz5OTYPe4dhZevsSBeUOsPNXCTakLcfaQ2hRcRzNsvqQVgA+ER3I3nuaaB6T59lAyzJ7At65raaYk+DPfjtTm2lczaJLLa0tyUpPwQ6lQHqrAY7wraX265ZBeMjtvuhl3+ZeXlJluPGNGj3F0qeZajKcU02S3yNKcQlKlhHXbfaoVLAY/xdNZZGTExrSPKZt/LstItKi0wpbMdptxx5DzqktrH0ZpIAO/Mrb1GsRlfGxYMEj3Sbd8Vu9xRHuD6EMNNsx3Y8ZqBElKCkqdUXFASdiQE9QRsNuZVgPcLGi8myIsciw3NxKX3X/LVXyd5eoutBpxCpfi+OptTYCCgr5SkAbbAV837hR0JyNLzdwwxbaJAeQ6iHcJMVK2nWGWFskNOJ3aLcZgeH8AFsEDfrQZPRLUu76mIzaTc2IzTNhyuTZoAZbKVGKiNGdQXN1Hde7ytyNhsB09tlVHsOwLFsBYuUfFbcYbd3nqucwF5bniSVNttqXuskjdLSBsOnT4zUhoFVFpb9PTWsf/MLF/ZTVW7VRaW/T01r/lCxf2U1V2E3m/0I+ehNf3y10vtqW7SlKhUlKUoI3nenuK6jWZdlyi2pfRsfBeT6L0dZHw219we3TsdtiCOlRPSLFMn0zbmYDdpKrjaG+aTap4B6IPw2VAk8pB6gDp1NWhXy5+pq+0axOxiUU0i+lRhn3PW78GbqW1EtIvpUYX9z1u/Bm6ltT4P0e30Y7nLDbzRzR3FKVVEziRwa2ZrPw66WnI4rNuvDVhfva7Ys2tM91ppxDJkJ3CSQ+2N1ADdQG9Uuy16VAbprxpFaUuqk55anCxcotpeTHeDympMl3wmUqCNyAV7jm7DY7noakVhzjD8ouNwtOO5Jb7jMtSgiaxGfStbBO+wUB26gj5D7KDOUpSghGLrDeomeOlJPIq3b7dSdo2/asO7lGpWfPqh4PaTjVqC+R283Vjd9QB2PgRz3PfYr6dO3rrNYkP8AGJnat/8APW8f8KmprUuD3uelX80p8N5k89XzShmGaVYxh8ld4Ifu9+kD9MXi5L8eU4dtiApXwE+rZO3QAHfapnSlVKClKUCqd0w/yg9af4eO/gCquKqd0w/yg9af4eO/gCq3o2Vc31h6eA9HxX/HH/bbXFVTazcQVr0ev+O43Kx5dxl5IiS4wtdziQGG0sJBVzuyXEJ3O42AO5q2apzWXRCVq/kWNZhjmb2u1TMZE2MkTLG1d47vi7IcSptbiAFJKNt+pBBFaPMZ+Hr1pj4UVi+ZXbLTdXmmVvW5yWh1xhTkUyR6bZKFo8IKV4qSWzyq2VuCK63+IzROLj7OUSNQbei3SJC4rbhS5zlxDfiK+h8vOEhv0yop5Qkg77EGqyu/CbadQsiuGU33VFNxuztkawy4It9uZYiN2pMdQeipYQs+G6uS6uR4ilKKAG2gnkSrn5x7g7kYfCgzMQ1Et9kyKGucwqbBxKI1DchS2GGXUeShW5eCYrC0vKcVstKt0KbV4NBZGYcRmkWGYlPzGblbEyFATJ3TCSp5bqmC2HUoCR6XKXm9z29MHtXGL8RGmWRs3d12/R7cqzypLDzchfpFpqSI3jAAdAXSlPL8IFQBA3qtLrwYLuZvFuVqvPFlnR7mmFEXamVPRpM1LHiPuPBQ8XZcdKggJQNlKHTooZGBwp4v54sUq+Z0qbdrblFyyaWiPHRHTcfKnUyHIi2itZDKXgy53J9BHUb70Fu4nqjp/nN1uNjxPKYdynWoJXLYaKgpCCpSAtO4AWgqQtPMndO6SN6lVUjoVwvY9odk90yO23ODOVJhebISm7HGiym4pfU8rymSgFyS4VFA5voaNm0nw+bdZu6grHiS+k5fP4yF+FtVk8q1LjYyqLjdmtci95JJjIdYt0cdkHoHHF9kI3B6n2VjeJL6Td8/jIX4W1VhQYsZKGpaWGw+thCFOhI5ikDcDfvtuTXSfMjnn6PTu/02107ny21e2fSy4ZJc2Mr1ems3mcwVKh2lA/6Og79tmz0dWPrl7/7kkWYAANgNgK5pXN5hSlKBVYyeIHEm8/umm8DH8rul0ssiLGuDtvs7j0aKuQgLb53R0A5TuT6gDVnVq1eOGDJ5HELk2rj+G4pkUO93C2TIL8nMrlapNvEZpKFbxmIjjT5Kk8wCnADsAdtzQWNmuuWkkmyeZcgsk/JYl3kXm3PWlqzKneK3a5Co09x1kggstupCSo9Dzo233rMJzbR3SvSuFmdmjWyz4o+hnzbHtEBLflLkhQDTMeO0kFbri1ABCRuVH7ZqoM24Yc9vNvisM2/D8hS1dsruCYs+6yrU5DXc7uudFkxp8aM5IQ4hBDbrI2Qvf4XoAmaZPodnN50h0/sPurg3PONO7vbMiizJwW3CuEyLzpcZeIStxLa2nnkBwJUtKuRzlUUlJDLO8UOl0VuQm5KvVumQmp7sqBMtjjUmOmHGEh3nQe27R3T1IV2FWKcuxZM6Ra3Mjtjc2JHEuRFXLbDzLB/zi0E8yUfviNq121G0E161eNwueXXjCLa9JtV/tcG1wHpDzUFE22+TNFUtUdDkhRdJWslpAQkAISo77w258FmrUjUDMb0znVtk22/3G93KLKk3R9LyUz4nhoiLipjeihpZ8MOeUrBabRsylXYNpV6taZpkWOMjO7E8vJLgu1WvwZ7TglS0NKdU0gpUQVBCD09pSO6gDLa1tsHDRk2LZlZshtkXFHYNrzK235MMuusBmK3ja7VJLYDCh43jrD6U9ErCE8y0K7bJUClKUClKUClKUCqw05+m7qh/tFr/AAdVWfVYac/Td1Q/2i1/g6quwu83+jHz0pr2+W+efllSWq2jWo2sHERm0Cw3C3Wi2R7DjqW7xN8tMqA4XZqlrgJacQ14myE85Xvt6HQ9qx+a8Qesdpuc/A8VnTnr1YIua+cVrsalqZ8mSlVkWpSm+RRcb5lp2J8QA777VfWccSWmOneYScMyhy+tyLfEjzrjNjWOXKg29h9Sw05JkNIUhhJLTnVZAASSegNTx/LMYjNOuu3+3gMwTc1pEhBUIg/z/KDuW/3221QqWr161U1hxrWVOm1jz+dlV5tdyssZVjdsjDbVxt8hormzHZDbSQwWhuobLABShPKS4N4TE1916k4KzcoeeTVyRarXKyaZdcaXb0Y7dlrCZdtLghuBoJPOCXGXC3yJKlALCjuJi110+ubzeU4xcLcuRmMRi5IdQ7yuz2EtgNuhCjzbBBSOw27HrUpoNFLNr9xV3fNMJhy4qLJGuVqx96PCusF1ty+rdWsXJ3kYgvdU7DcB2P4SPDcUnlc6b10pQKqLS36emtf8oWL+ymqt2qi0t+nprX/KFi/spqrsJvN/oR89Ca/vlvpfbUlGR51lNkvD1vt2l96vEVsJKJkV9gIc3SCQErUFdD07eqsZ77GTI/VtF8wSf3iGF/1OVZFKhUqze1fuSm1tPaPagICgU8zVvbJG/rBDnetfpPE3qViGSTLUy+7cYMR5bbce9w0tyk9fgu+GrfmT279duw7DctxAdbU2okBQIJB2PyVFrVpVpzZXHH4OG2vxXXPFW68wHlle+/NzObkHf2VlhVmCcUF3ydQZmaTZDKLadnnrMyqSAv1egoJ5R9tZq9Ispc23olrhyIpdb5yy+AHEbjsoAkA/LXpSlKEhKUgADYADoK+Xv1Ff8E/1VrVsknYiukf0qML+563fgzdSpTzSObmcSnkAKtztsD23qLaR/Spwz7nrd+DN1Q3E5gGoOV6qWPE8TiXg4/qbakWzI7jDDiW7V5nkmdHKnE9G/KUvyY+5239Addtq4YT0e30Y7nLD7zRzR3NpApJJSFAlPcA9qoy68PmW3vJsganZ9bkYZkWVRsrk21m0rTPU8wzFQhgyi+UeHzxELOzQV1I3rXjI8i4nMO0uOT22wZtHzfJE3K4u+SWx+YkyoTDTMWO622y4pAcWhxSQQ2hSV7lfYVLNRcm4n4kO+ZJY7pl0eC/l86C0yxj7shyJbmoqFxVssttKeWlx9ZSpfKU+jsSkbmqHZmce4KcttORLyWXqxarhOZatbLZdsThSVQrkichbiTJI3V9EQUo5EDnSUpHpBU90N4ccn0o1FvmeX/UGLf8AzvbU23wm7c7HWAiU6+halKfWncB5SSEIQnoCAOu9VWmRxO2G7XzOLfDvz14vl/jsSrI9bimAojDYS1yh0Vyjy5oNAhfIFoUjcqUa9uP6p662CfZ7zdoGdXnDkzn48l93F5JuTj7lnU4G1RUshwMonJLaHeUI3KQV8uyyG4NK0Xb1P4worMpcOx5PdLu/hUWWzHdsDrDESX5HGU8pfO34br3OqQUoS4HCtPIpoAAnYrhkvOot6wa5SNRJdxluNXl5q1yLjbHoMl2F4TRBW28ht07PKfSFLbQSEjYEALUEqxIf4wc6P/eYA/4Rv8dMhumrES6OoxzFLHcLcNvCceuKmXT7d08pA+/TEP1/558UuCP+DaqaVLg97npVfNLhh/Mnnq+aVcHLtaWf1TSCE/8AxOQMp/8AyTXWrPNZU9tBnFfayaH/APurLpVTu001H1d1WwvO3EW5ubjrjqA+5Z3rkxcmkLV3OyNwnfvynqO/YiplgHERrNeUMpkaUSb+yfoflMJh1gKX7VOFKm0/eFbARMOxSDNVco2O29M1bhdVKMdKnis9z4hBVv8ALWZrObGTFY/drpdonjXbGJ1leSBu1Jeju8xI68qmXF7gfHyn4qrLTD/KD1p/h47+AKq4qp3TD/KD1p/h47+AGtqNlXN9YepgPR8V/wAcf9ttcVaiHB9cray57nzlVrRBu+QXVmLBkFpmS7IywuoLqQdnEqguuLAPTlO/etu6Vo8xo/F061305TNjYjEzkt3i8ZLcLd5FJCy7enb455O7clKIPkq4CGlpUs8m5dKtlKbBzN6wbiWmYxOnjLNQGr15kzO4tMxLiUINzaXFFmYSkdAhSS+Uo7K2PNUmVr5qZYM5lv38JmWKTcr3EtEeLFjLgXFEQPllpie06taZWzB8Rt5tICkPIBJSK7rvxvWiLAt+RWPTy43PHJrz7RvHlJRGaDAih7nWltaGiHJK2wXlNN7sLJcT0oK31ag8WlghXXH8Df1BnIgybm9Zbil0y3Jbgix1R2nOVbauUueOQt1fhDYp5FqKUnpn4PxFWTULMbliNly4+Leb7cFSnHQoLiSRAW15E4s7BfhpfSlAI5VICSAQBU8HGrebCyWch0pu12mi53QOt2FmTMLNuiz1RQ7sywvdwlKjyrKEnbovrtWcmcXN9i3KWlvSBblojTrywJxvqErVHtl4FrkPeD4RIJfUkpRzdUk7kbdQgi7NxPXFiXNhT8/i2q32HJrhjjb0sonPyUzIXmtqen4S3C0Zeza+vJtz7KBA3MrgHcA+2uaCseJL6Tl8/jIX4W1VkQ/+psfxaf6qrfiS+k5fP4yF+FtVZEP/AKmx/Fp/qrpPmRzz9Hp3f6ba6dz5bbupSlc3mFKUoFKUoFK43HtFNx7aDmlKUClKUClKUClKUClKUCqw05+m7qh/tFr/AAdVWfVSyJF4001RyC/SMUu91sWWMxXRMtUdUtyJJYQUFt1lA5glSVApUNxuCDt0q/BRp0XbUedVTq9uVVM90SlxE6NVFc7InX1TCOaiaUawXPOs+uGDPYsi06hY/bbFJk3N17x4Ij+VpccQ0hBS5uiWdgVJ6pquI/Btl7+rLWT3/wByk+yRJdwG5hR/Elw37LItzbToMYvqV9FQXAuQpohA5W+ieXYf347N+1DOPmzM/uU9+Oy/tQzj5szP7lc9w4nkS23VZ5UNZsS4NdT7Nn+n2VOuYhbY+ISLMt1FsjstlTEOMuO62lfk/jlTnOpZ2eS2eZQKCfSrdaoF78dl/ahnHzZmf3Ke/HZf2oZx82Zn9ym4cTyJN1WeVCe0qBe/HZf2oZx82Zn9ynvx2X9qGcfNmZ/cpuHE8iTdVnlQntVFpb9PTWv+ULF/ZTVZ86x2f1YfnBP3MzP7lY/RuxX1d2zLU3IrJIsknOLhFlR7XJWlT8WJHiNsNF4J6JdXyKWpAJ5d0gncGqLVmvDWL03Yy0qYiM+GdKmdnNE/7MOdVym9ctxbnPKZmezMfVZ1KUrzFhSlYPMMzx3BbM9fckuLcWO0kkAn03D9ahPdRPsoMtLlxYMZyZNkNsMMpK3HHFBKUJHcknsK8lsvEO/WVF4t5WqLJbUtlaklPOjrsoA+o9x7QQa1RdzzKeJrUi3YdED1sxZlzyiTGaXspUdB3Wt1Q7qPRKR8EFQ+M1tsplmHb1R4zSGmmWShtCBslKQnYAD1ACta9VMtap1Sjmkn0qcL+563fgzdSyonpH10pwv7nrd+DN1LK44TeKOaO5zw+8080dxSlKodilKUClKUELw8f+3meH/v0Ef8EzXXdswu+Oaj2+y3oMiw35nwYD6UEFuancltaidjzj4PbqNupNd2H/r4zz+UIQ/4FivZqJhcfPcUl2Fb6o0k7PwZSTsuLKQeZp1J7jZQ67ddiQNt6lwe9z0qvmlww/mTz1fNKTUqHaWZlJzDGUqvDIj3y1uKgXeP9ZKb6KUB9ar4Q26ddgTtvUxqp3KUpQKp3TD/ACg9af4eO/gCquKqjyLDdRMK1Dv2p+l9steQIyeFFavFknzVQ3TIigoZejP8q0DdtZStC0j4CSFdSK3o4Y4/GHpfw6qmab1mqqImujKM9UZxXRVlM7I1Uzt1ZrcpVL++TxLfuaInz0ifk6e+TxLfuaInz0ifk6aE+zrg/Sr/ACqP7tv8kmGgulUHKrlqDjmE2azZdcg+tV7iwW/HbkPJIdkJSoFAeWCedfLzLHRRINeC2cNekEfELBh99xGBf2MfS74L1wjoK3lOrC3y6EBKVpcWEqW2QUKKU7g8o2xHvk8S37miJ89In5Onvk8S37miJ89In5OmhPs64P0q/wAqj+7b/JJLlw76G3iaLhctLMckSBNcuBWqEn0n3FhbilDsoKWlK1JO6SpIUQVDes4vS/TxxpxleH2sod8r50+TjY+VShLk/wA5IAdV7Vjeq/8AfJ4lv3NET56RPydPfJ4lv3NET56RPydNCfZ1wfpV/lUf3bf5LnAAAA9Vc1S/vk8S37miJ89In5Onvk8S37miJ89In5OmhPs64P0q/wAqj+7b/JmuJL6Tl8/jIX4W1XuynJM3w+VGvsazN3nGBDQJbEVJ8tjLHd1I7OJ2I9EdRsfliNwtet2sUWPjebYXasFx9M1iTcii8IuUua00sOJZbCGwhtKlJTzLKidtwB66uxKEoQG0j0UjYD4qzVqpilti4ixhLeGmqJqiqqqcpiYiJimI1xnGf8s7Jli8aymw5fa27xj1xalxl9CUn0kK9aVDulQ9hrLVXeTaXSWLsrMtNLoiwX5Sw5JZKCqDcwPqH2h2J+vT6Q3Pr2I9WHaoMXicMXyy3Lx/J207uQH1boeG+3Oy52cSfi6/11zeWnVKUoFKUoNXcT05teX656jWBGSXOyS7AmLcX3rSzCbkSHbjNuTm7z7kdbx5WWo6EgLASlIAFTR7hZtkhxb8jWbV195agrmVnNyZQn4ghh5tI+9WH0Ujyk8WvEbMkbhp1eJx4/sKG7WVq2/+581sNQVbA0YvFjAGPan5KyUpI559zn3JRO3ciTKWn/dXHD/lt8yezZRb8jyBy83DGMjfsciWtptrmcbjx3FgJbAAAW8sAHcgbAkkbm061w4KhOVG1wlTub9Ma1ZWWub/AETbrTSdunb6HQbH0pSgUpSgUpSgUpSgVxXNKBSlKBSlKBSlKBSlKBSlKBVL6x22xajZLC02tVriTL8tsOT7g414gtELfcnfsHFk7JHf1nbdO811Jzp3FIcW02NlEvI70sx7XEJ7r9bivYhPcn5K9GneDNYTaHESJJnXe4ueVXSesenJfPcn96OyR2A+Wgh+gujQ0tbvcmbs5Mmy1NMuHbcRUE+H2+u3Kj29Xsq07goIgSVq7JZWT/8A1NeiuCNxtWKo0omGJjOMkU0kP+KrDPix+3D/AIZupZUCiWPKdOwqNisXz5j3MVNWtbwbkwknqUMLX6K0D6lCynlHQK2AFe2Nqxg5kt2+83b3Pz3dgiHe0GA6tR6bN+Lsl3r621KHx1FZxFFi3TavfyzERGvZPNOye/jhNavU2qIou/yzGrXs907Pr7EwpXwhxt1IW2sKSobgg7givuronPXCopSuCQBuTQc0rA5DnmGYopDWRZPbYDzg+hMPSEh534m29+dZ+JIJrDry3Kcl3j4ZjEuGwvcG63phUZCR7W46tnln+GlA+M1NVi7VM6MTnVxRrn9vflDjViLdM6MTnPFGuf2976wwlWb58eXYC6RE7+3/AKPjfjqaVhMTxhjF7cuMJb0yVKdVJmS3tvEkPq25lnboOgAAHQAADtWbrOGt1W7eVW2ZmeuZnL3ZliiaKMqtucz1zMqszAHTfUCFqBHTyWa+qbtl8A6Jbc7MSD09von4tuoAq0kqCkhSSCCNwRWPyKw2/J7HNx+6shyJOZUy4n4iO4+MHYj7VQvSHIZ4YuOnWTP81+xRwRnFqPWVEUN2JA9u6dgepII67E7VQ7LFpSlApSlApSlApSlApSlApSlApSlAqP5jguOZ1bTbr9CCynqzIbPI8wr1KQsdUmpBSgqlrJsz0mlIt2eqdv2LrWG42QMt7yIiduiZiB3H/aJ+2e4AzOnmr+MZ9dbxj8Gcx5wtMlxAQlwFMqOFbJfaP1ST0B27HbfoQTms5xB3M7K7aGshuNp8VCkKciKT6SSNiFAg7itVr1w56t6YXljKcIeF48hX4rbkI8shOw67tH4QPbZJJO/assNzKVBNJtUIWpFmX4zKoN7txDVyt7qShxlz28p68p2O3yj1VO6wyp3Hn4Vn4pMrsTXKJF9xqHfndgdyG1piJJ9X+b29farXl3a1wCEzrlFjFXYOvJQT981UepPDknP9TXtTI+c3Cyyn8ejY64zGaCgqO1JfkK67gjnU8nfY7jwh7TWpmR4pjee2TI24wgW9nFp1ys89OYZeyTDm+SvtR1yG5TSVxGfFcbkBTbq1HwkAAhSikNzsq4mNAcKXMYyXVzGIkm3tlyREE9DklKR7GUEuK+0Ek1DeEvN8FzWLnM/T26m4WuZkky8+MqK7HUVzJL6zzNugLSdkg7KSncFKgNlA1DdMss0Qh5liumt0GmmXrvSHPc/c8fZcubTEhpJWppTry3+TdKSpKkuAApIIHQna5tLaEhLaQlIGwAGwAoPqlKUClKUClKUClKUHBqm8Wt2X6uO3nKLlqFfsftrF3mW2226zKYaCWozqmVOOrW0tS1LWhR26ADarkNVvoF+sif8AdJfP7Rfr0MLXNnD3L1HnRNMROUTlnnnt5oSX6YuXaLdWzKZ6svFiW8Px965myM8R2WLuIdUyYib7ALwcB2KOTwObmBBBG2/SswdHpw6HWXUL/wD0Iv5tWtemWH3LG9ScpmZHii48iRmeVzY0ljTIu3JDT9zmOxn2ryXSNy2ttaCWiAClHXbc/Nnh8SV7awbI9Snc2OT47nSlhpiGw3DMB6wzmoT60tpUDu8ppuQr0eVUh8coSGynH6niuV8I8Gdx2OT3tlveenfZl1D/AKfF/Nqe89P+zJqH/T4v5tWrumA4vc2ZtmNZZleb2O33G7W5F4ujCGhcIpMOaqaltb0NtDTRdTGSAlCwgqHIupDkkjiixld4vtsvOc3RF5OSpchhuKUWxpm8rbt5i/pdZb3h7K5lJdUpJ32JCQH6niuV8I8Dcdjk96/FaTuoktw16258l95KlttG5RAtaU7cxA8n3IHMnc+rce2u33nZ/wBmTUP+nxfzaqF4bYuul71Ox2/6p2y/riWP3YW6DMuiSpaYDxsjsQLdU00t3mUmXyLW2lRDZB+DW4NP1PFcr4R4G47HJ71aSdH78lhw2vWzPGJfIfBcffiPtpX6ipsxxzD4tx9sVl9HssvWa4BBvWSMMNXdmTOtlw8n38JcmHLeiuuIB7JUthSgPUFAeqppVbcP30vZP3U5R/bs6uld6vE4Suu7rmKqYicozymK841c0NabdNm/TTRqiYn4TT4ysmsHmWX2nB7BIyC8LV4TICW2kdXH3T8FtA9alHoBWVnTolthv3Cc+hmPHbU664s7BKQNySaq/FbfJ1WydnUbIITjdita1DHYT3ZxXYzFp9p29AHt377beYsZTTfEbu5Pkaj50w2MjuqAlqP8JNti90sJ/fetR9Zqw6UoFKUoFdMqJFnRnIc2M0+w6nlcadQFoWPYQehFd1KTGYiB0k06Q541vxePanD3XaVuW9R+2Y6kE/LXyvS2xb7xr1lEc/vcgmL/APUcVUxpU24sN6unqhw3NZ5EdUIYNLrYT9GyfK3U/Wm9vpH/AISDX2rSfC3k8k6PdZ7franXqbJaV9ttx0oPyiphSsbiw3q46oNy2eRHUxFixHFcXStON41a7UHPh+RQ22ef7fIBv8tZelKopopojRpjKHammKYypjKClKVsyVWmq8CZjlwturViZUqVYwY9zaR/7zbVq3Wkj1lBPOPl7narLrrfYZlMORpDaXGnUlC0KG4UkjYg0HVbrhEusCPc4DyXo8ptLrS0ncKSRuDXpqr9NJD+E5LcdJLm4rwGQq4WFxZ/VIalek0D7W1HbYerb2E1aFApSlApSlApSlApSlApSlApSlApSlApSlB4nLNanbk1eV29jy9lJbRJCAHeQ90FQ6lPr5T03AO24Fe2lKCMak6iY5pViEzNsqVJFvhFtCkxmS66ta1hCEoSO5KlAVS18xrH9Q8z98JnRmxx7rMjIiv3G6ylOLmweX0fFjMHw3FIKgOV7m2SRsdu175fidnzbH5WOXxjxI0kAhSTstpxJ5kOIPdK0qAUD7RVN45wx3LzYza86ztd1ZjBlKOWN5SVFl0rbUWpheiIJSQN24qHU7ei6OmwQSMjT7D7CphN/jsQllBdi4Yy1ZbcuQ26AUh2IWwlauqShUnff6g9qmOizdwtedoawPTaRY8RnmY3dXlMmO2882SpiSW1BJMg7ltbhBU6OVSlq5E7W7j2mGC4zIE622Bt2cEqb8vnuuTZnIVcxR5Q+pbvJv1COblHqAqVdqBSlKBSlKBSlKBSlKDg9qrfQL9ZE/7pL5/aL9WQarfQL9ZE/wC6S+f2i/V1r0O70qPuTV+kUc1X2sDYuKPE7zlLuPysFza028ZFNxaPkM22tm1SrhFluxVtodadWpILzLiUqcQgHYdidqlF3170dssOVOl6g2dbUK5Q7RJ8CQHlMypTwZZQsI3KeZZ7noAlRJASSK5Rw5Z/KZOKXbPrEcRRm10zRpiNZnEz1OyblIntMuPLfU2UtuyACUtgqCB23NQfGuCnPrNPul3umqdnukyS3YUxi9ZnvDCrZeE3BJWjx9tljnaKUcgTzbj1gwqWztn1AwfIL9OxexZZap93tg3mQY8pC3mBvtutAO469KkFa4aS8LmXYDre5q3kGfwLswmDdILMNi3OMrCZcpD4JUXVIHIEcuyUDmJ3771sfQKUpQKrbh/6aeySe3upyj+3Z1WTVL6b2S+5Ho5PstgvYtL0vK8mbdlBHMtDJv07nCOvRRG4Bq636Dc6dHdWmr9Jo6NXfS9l3ec1ryheLwHXkYVYnwbtJbPKLpKSd0xkH1tJPVZHc7D2Kq2WGWYzKI8dtLbTaQhCEjYJA7ACsfjeO2vFLLFsNnjhqLEQEJHrUfWon1knck+01k6hUlKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoIFq5ityu9mjZNjGyMkxl7zhblbfqwH6rHO3UpcRuNum55dyBvUkw7KbdmmNwMltZPgzWgsoPwml9lIV8aTuPkrM1S03IoGhuXXcTnEJxrIGn7lEAUAGp6ElTjI9QLm2439fyCgumut+QxGbLsl5DSB3UtQSB8prGYjkMbLcXtWTRAkN3OI1J5QoK5CpIKkEj1pO6T8YNVNaMRtOsuomeTNQfKLnbcauSLBbbQt9aIjSBHYfceUhBHO4tbg6q35QnYbbnfamnPOZWYTDUX4ruXKsqaIznKM51zERERnHDPHs6lw+frH+zMH+kI/HTz9Y/wBmYP8ASEfjqAfoZ9CPsa2r/wAz+9UE1BxXhF0vuTFpy/AXUSpEJ65ctux263MMxGlBLj7yojTqWW0lQ3U4Uj4+hrOVHHLrofw/l19mn819efrH+zMH+kI/HTz9Y/2Zg/0hH46rK06C8N1+t0K72XC8fnQrjHRKiSGHlLQ+yscyXEEL2Ukg7giuqVoZw4w7pBtD2ncBUi4h4sqajSHWh4SQpfiOo3ba6EbeIpPN2TuRtTKjjk0P4fy6+zT+a0vP1j/ZmD/SEfjp5+sf7Mwf6Qj8dVf7w/Dp518z+93b/H8m8r5/Af8AA8Pm5f1b9T5t/qObm267bda9v6HHh/JSn3vbNusbpHOv0vtel1plRxyaH8P5dfZp/NYfn6x/szB/pCPx08/WP9mYP9IR+OoB+hn0I+xrav8AzP71P0M+hH2NbV/5n96mVHHJofw/l19mn81kR5kSYguRJTTyQdiptYUN/krurX3VHCMc0RiY7m2mEFVjkDIbfbpUWO+55NLjyXg2tLjZUQSAdwe4IrYKsVUxERMNMVhbdq3Res1TNNWca4ymJjLPhmOGNeZSlK1QlKUoFVFxLatX/SDEbNesek2uK9dL5Gtbsq4WqVcm47TiVkrEaK4266r0AAEq9e9W7UV1C05sepNugW+9TLnDVbJzdyhybbLVGfZkICglSVp69lKHy0FGOcSWpUGJigtsKw5jJyWx5NdWfJrLNsZedtxjpYZSzKeccRzKdcCirfmATygeuUcOGt+V6oS8jtWXzMckybIxEkHzbb5lqlx1uhwOx5MCYpbrZQtohL3Nyug9EpKSKkdx4c8Av6YvutmZBkbkOHcre09dbo484I85LKX0c3Q7fpdsp+tO5Heszp9pBjWnU+ddrdcr5dLhcI0eC7MvFxXMeEZjnLTKVL7ISXHDt7VE0FYY7rLrdkllTqrBtOEKwabLu0WPb1KkNXSMzFL6GpS31rDbxW5HIVHS0lSUuAhxXKqoxiPHTZI2Gs5DqRbfEuMyPZVx7dZY7bS1LlWGJc5BCpMkJUhBkr23UlWwSgBauqrWRwyaZJvC7mrz25F8sl3Fi0uXN1Vuiy5KVJefaYJ5ULPiOEEditRAG9Yd7g30UcszNlYgXWMiOmIlp9m4LD7aY9tatyEhZ3IBjMNpV7SCrvQeP9GTgEqY23aMRy2bbZEmFb2L2mGyi3qmzICZsVgqU74oUtC0oJ8IpQtQ5ykKSo2PovqBO1T0vx7UG44+5ZX75ETLMFxxDhaCidhzIJBG23XofiHasMzw46WR7U3ZI9pktwmrxb74hpMtewlQorUVg7k78oaYbBT6yCT3qX4FhFl04xSDhmOrlm221BbjJlPl5baNyQjmPXYb7AeoUEgpSlApSlApSlBwe1VvoF0wief/AKkvn9ov1ZNVroFscInjf/4kvn9ov1da9Du9Kj7k1fpFHNV9qmmuJXUGx6lzHMzfjRcT883aNFQ3a/FhSYEVbzbSo1yZWtC5aiwSuO6GylRUgdU9ZraOKlL2Q2DFcl02uljueRXO0xYbbkxp5JiXKNPejSSpHY72yShbfdJ5SCQalf6GvRZWRv5O9iLr78ibJua4ci7TXrYJkgKD8lNvW8YiHl86ypxLQUVLUrfcknzJ4WtD02h+ynF7gtt+VDmJlOZDclzozkTxBG8mll8yIyGg88EIZcQhIedAGy1gwqUIk8ZDAmT2LXpZeLi1bmGVOrZmshSpMmeuBDjoSrbcuyEpTzEgIC9zvtX1m/GNE04uEGwZpprdIF7Uh6VcIKJjb5ZiIeS0H2FNpPlAVzBSU7IVslW4Gw3ntu4Z9EbXj0/FYmFA226W5q1ym3rhKeWthp1TzWzi3StLiHVqcS6lQcSvlUFApSR45fCpoVPjsx52K3CRyLcXIddyK5LeuHiLQtaZzpkc85JU03uiSpxOyEjbYAUHXplxGWrUrU/ItM2cdftcqwiQseWSUtyXW2nUthwxVhLgbcC0rbcRzoUnupJISbgqAYloVpfg2Wv5tjNilRro6mYlHiXaY/FiplvJfkiNFddUxF8V1CFL8FtHMR1qfbj20HNVtw/fS9k/dTlH9uzqsiq44fvpeyfupyj+3Z1XW/QbnTo7q01fpNHRq76VkUpSoVJSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBWunEhoEq/tSM8wyITcW0886G0OslI+rSB3WPWPX9uti64oKI4P8pN207k408ol2xTFBA222ZeJWn7Z5/F/wB1SPRb9durP3ZH8AiVlrTpoximpcnM8abQzCvrCmrpFSeVKXgeZLyEjpuSNj9sn1msTot+u3Vn7sj+ARK3p2S9PBeiYno0/PStWqi1KxLVxeplszrS9rGnuWwybJKF5ddSGi5IadS6lLY9Pbwzukkb1btU5xT3CXA07hGNkU+ytu3mKmRJjSZ0RtbXpczT0mB+mI7aum7iOxAB6E1o8xSsXgey+055a71DzUSmIFttMGLclPeDItzUKAIymGkhsuBt1wLdKUOoSS84FJVvvX3+gzyyfCRGctuH2VvzJeLRLj2rxmkz3ZVtRE8qdPbxHFIKlkJ32PpFZrqxriRz3DcHtTTVrnuQ5VivLlrkXnyy6vzLmxeG2GWm5S+V16OY7q1NqdAcU2hKlKJCifBcuL7V2Lj93u8W84k8W5iYy3Pc9MLViByK321HlBD36ZU5HmSHEpRyEKj9AoGgyVq4Ns+j2eMxOlY4/GhqS75iU2ExJjKZvlAhSA2hLakEdSUtpQVBO6O+/bbuCnI0PPX64O42m8NxWxZiwyoIsRN+l3Ax4iiN222o8lEdBTt6LewATsK+rhxPa3Q+dmPGsslUNThtrqcelhGXcsxtoNxR4v6VUW1K6qLg3TzfB61ncM1H1vyPVfA7ll2RRbdjt3vmX2zzPGsj7A5IMyRFiB54vKDiltsBxKihKd1bgHoaDailKUFN8U/6wbJ911j/AAtFXJVN8U/6wbJ911j/AAtFXJW8+ZHv+j07/wDT7HSr+wpSlaPMKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKqVem+quGXO6u6Q5njUe03ma5cXLXkNnelJiyHOrqmHWJDSghavSKFhWyiSDsdqtqld7GJuYfPQyynbExEx1Tm5XLNN3LS4OKZjuVN5BxW/tr0o+b1x/PaeQcVv7a9KPm9cfz2rZpXbd1fJo7FPg57lp5VXanxVN5BxW/tr0o+b1x/PaeQcVv7a9KPm9cfz2rZpTd1fJo7FPgblp5VXanxVN5BxW/tr0o+b1x/PaeQcVv7a9KPm9cfz2rZpTd1fJo7FPgblp5VXanxVKqy8U05tyHJz/AE1tyHkKR5XCxma4+ySNgtCXZpQVA9RzAj2g9qnWA4TadO8Rt2HWV2S9GgIXu/Kc535Dri1OOvOK6ArccWtaiABzKOwA6VIKVzu4u5eo8nOURtyiIjX7cojPLOcs9mc8be3Yot1aUZzPtmZ7ylKVM7FKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFVVot+u3Vn7sj+ARKtWqq0W/Xbqz92R/AIlb0+bP8AvC9PBeiYno0/PStWojqvmMnAdPrxlsPHPPrtvaSsQC6ptLgUtKSVqS24pKEhRWohCjypOySelS6sFm2HWrPcdk41eH5zEeQpCw9BlLjvtLQoKQtDiCFJIUkGtHmKqw3iawm52FNxzxNis6kyp0eI7abgu6wH0xYrUhwofLDSm3ORxQ8FxtCyWXCkKSAoxLJOIDhytOG3SyY/hE29xrVfrSqTaWrLIaSZbt3jIbeBU36SmpLrTmwBJWkAdSKkV/4TrDco0C1Rru5NjSsrYyrI5t6W9LuFweZYbYSht0LSlsKZaSyoFKgUKV03JJyV44SNKL5fL7kMw3pM2/Ftbq2bitvwXG5rE1DjfL9UmRFZWCd9gkpGwJBDlziw0GbnXO1pvUtyVYXPC8Bq0SFrec8qTEKYyUoJeUH1pbIb3IJqQada76c6o3teP40zemprCJryU3KxyYQJiSfJZYQp5CQpbUg+GsDqFbg+usFa+ErSC03edeY0CcXps5Fw2XJJDLyZyJp5Dtvsp9tKiCT06dulTXGNJ8QxG9t5BZ48hEto3lSVLfUob3S4+cJfQ+2R1H1o6DpQTKlKUFN8U/6wbJ911j/C0VKMp08v8m9P5Xg+cT7JdXwjxo736Zt8jlSEjnZV8E7BI5kkbdTtud6i/FP+sGyfddY/wtFXJW8+ZHv+j07/APT7HSr+xWLeqeTYkRF1Ww16CgHl88WkKlQXPjKQPEa327EH2kip7ZMisWSQ0z7Bdos+Osbhxh0LH+6vetCHElDiQpKhsQRuCKgd80axidMVeMcfmYzdid/K7U54XMf3yPgK+UVo8xPqVV6si1dwLplWPt5laUd7jZW/DmoHrK4pOyu+w5D2G5qV4lqNhmbtqVjl9YfebH0WKvdqQ1129Npeyh19e2x9RNBJaV4IN9tFymy7dCntOSoC/Dksb7ONnbcbpPXYg9D2PqNe+ggWtmqCtIMGVmKbUxcFecIUBLL0hxlG8h9DIUVNtOr6Fe+yUKJ7VAXNdNb4zqPK9BIJYXv6ce6Xp5YHq9FNk2/8VSHiesSb/pb4DiQW4d6tU9zc7DkYmNuHv8Sas2yy0z7NAnIIKZMZp4EHfopIPf5aCmJPExfra0ozeH7Uic8kfAtFhmPJJ+JUhhisVZeMiNMzXGcLybh+1XxFeWXIWq3T79aY0aMt8pUrYkPlfwUk9Ek7DtWxNUxxBWNmdlWlWRSB9DxzKDOKjtsCYrrY3JIA6roLnpSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlApSlAqqtGCEZnq1HWeV0ZeHSg9FBCrfF5Vbew7HY+vY1atQPI9H7FessGdWi+XzGb840iPLmWWSlry5pAUG0yGnELad5OdXKpSCpPYHYAVvTMa4nhX4K9boou2bs5RXERnlnlMVROuOLVlq6pTylQP3s8h+zTnH3rb+aU97PIfs05x962/mlZ0aeM3Lh/Xx1VeCeUqB+9nkP2ac4+9bfzSnvZ5D9mnOPvW380po08ZuXD+vjqq8E8pUD97PIfs05x962/mlPezyH7NOcfetv5pTRp4zcuH9fHVV4J5SoH72eQ/Zpzj71t/NKe9nkP2ac4+9bfzSmjTxm5cP6+OqrwRbinUkYHYUb+kvL7GlI9ZPlaKuWq/gaOWpOTQMsybKsiymdaeY29N2kNeBEcPQuoaYbbR4m2451BRAJ22qwKxVMZREM4u9a8hbw1qdLR0pmcsozqy1Rw5RltnLm41KUrR55UKz7TvEsijOXiZjL0m6sDmYkW1aWJoV0G6HOZPXYD4R6DtU1pQaLZK1rfh+cv5o3ZsojvQUJSJkhgvjydI2CHXWwW1jbodz8Z69a2A0Y4j7DqEGLBkJatmQFGwBOzMoj/Rk9lHvyn5N6ugjfoaxN5xDFMicQ7f8AGrXcXGgUtrlQ23VIH70qBI+SssK84s7q5YuGzUW+Mgl232CVJb27haUbg/fqa6ZvLkacYo+58JyyQVq+2WEGo/rrh6co0LzDCYiHVJn2ORDbSSt1ZBRsOp3Uo/fJqsbJrVqtb8Ex+Dj+kDkQQ4LTLtxvUhTVvDLTQAcW6EhTXwevOgbVhlsnVE8Y9+VjOldvu7XR05PZoqFbdR40xtB26ewmqrVxMa05BcIcyHfcKxe1yYy5SvK4z1xivMNvKYddanRSsNoDiF7OOtBGydydqnF44XM/1EmtL1K4jb9keMCVFusWwuWqE2iPKZWhxtYksIaW6lK07gKTsQRuDtQbJUrgDYbVzQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKqziJ01u2omFw5eK5bFxrJ8RubWRWO4ThzQfKmkOILMxA2KozrTrrbgBBAWFDcpANp1q7rJIcw7WuJc83tE682rLHWrdjalradiW6X5OQsEOqbS2haG3g62pS1LK2Cwla1OpbCEwLXq3FtV2sFl1G0zwLIJ9wbfkTNL8J85NzQ+SQuYxNQpPpEn6Il3bdR333qydO75qnpjprbsdbsUJ+LY47rsiZkFyaYkOEvrWWGY8YLjR2UhRbaR44S0lCEBASkbcWm0avZVDjxbBiUXHoDaEBHipMdtlKX91IbelseMrZI3CFW1sHfo/8AVVKbbw4RpjwmZ5mE+8vBchQajFyOygOu+JslTjjr6R0AKA6Gz12QnfagtPGMituW4/b8ktDoch3FhEhpQIPRQ326eztWUrH2Kw2fGbWzZbFAahQo+/hstDZKdzudvtkk1kKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKCntZNUtRsV1EwTTbTWw4/PuOYR7tJU7eX3m2mUwkMr2BaBO6vFI7HbYVVOS8aeQRLXYbixithxpuWiXHn3HJ5Mhu1+dY0hbK7a3MbQGmVqLalJdfUhPKpOyT6W16alaMWzUfJcbzA5bkOPXnFW5rMCXZ3mUL5JSW0vJUHmnEncNJA6AjrUdRwv4pbIEKDh2ZZZjPgwHLbNct0tkm5srdW6syEutLQpwuOuq8RKUq+iKG+2wAQu+8V+SWrU3H8PkY5jtliXlu0rjsXu6eTvXUTOQOeb5Y/Sb6mCsbthwrc5TyD0k72dqTn2d2/LLRp1plYbRNv1zt8q7uybw+tuJFix1tNq3DfprWpb7aQBsANye2xjr3CdgvI1ardlGVwMc3tapWPtTm1wZRgeF5OVBxtTiP1BrmDa0hXL8Z3mWoGktvzq82jJ4uU5BjV8srT8aNcbNIbQ4qO9y+Ky4h1C21oJQhXVO4UgEEUFcTOJXJLBf4VgzfDYeNyinGBPZfleUlhy5yLm06lC2eZKggW1KkHpuHDzbEbV64vGZpDOhtPwoWVPyZkuJEt0FFlc8puHlaXVRXGUb7FtzwHAFKKeXbdYQNyPc3wm6XNswmC5eXRDFo9J2YFqeVbnZrrS3CU+kpS7jIK+2/o7bbdcbgXBhpFp3cbfc7Eq5eNa7hDuEXpGZCTFQ+hlCgyyjxABIc3UvmWem6ulBnNPOI+xanagxsOxvGr0mDJx9d684S4xY8F1uWuK7FdbXspDjbrTiFdxzJ6bjrVv1W+GaE4rgmXIzCwXK7NyAxcI7rDjyFsvpmTnZq+Ycm+6Xnl8uxGw2B3qyKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKD/9k=>

[image2]: <data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAMCAgICAgMCAgIDAwMDBAYEBAQEBAgGBgUGCQgKCgkICQkKDA8MCgsOCwkJDRENDg8QEBEQCgwSExIQEw8QEBD/2wBDAQMDAwQDBAgEBAgQCwkLEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBD/wAARCAGDAmwDASIAAhEBAxEB/8QAHQABAAICAwEBAAAAAAAAAAAAAAYHBQgBBAkDAv/EAE4QAAEDBAECAwUEBQkGAwcFAQEAAgMEBQYRBxIhEzFBCBQiUWEyUnGBFSNCkaEWFyQzYnKCscFDU5KT0eElY8InNDWDorLwRHN0lNLi/8QAGwEBAAIDAQEAAAAAAAAAAAAAAAIFAwQGAQf/xABBEQACAQMCAwQIAwYFAgcAAAAAAQIDBBEFIRIxQQYyUWETInGBkaGx8BTB0SNCUmLh8RUzNDWiB3IWQ2OCkrLC/9oADAMBAAIRAxEAPwD1TREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBFxvS5QBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREBHcxnroBZvcRWnru9MyX3V2v1RJ6uvsf1fz8vxUhCiuexMlbYOunMvRfaNw1MI+g7Pxd/ta+6O5UqCk+6iC7zOURFEmEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREBFc86dWDrpaWb/x2k148pZ0HbtOZpw6nj0b338ipSFFs9cxosAe6lG77Rge8NcdnbvsaB0/5E9lKR5KUu6iEe8zlERRJhERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERARbPJGxtsO54Yuq+0bR4sPidZJPwt7HpcfR3bXzClAUXzySONth8Srng6r5SNHhRB/WSTpjtkaafU99fIqUDspPuohHvM5REUSYREQBERAEREAREQBERAERV3nGakmaz2ybojZttRODrevNoPy+ZWSlSlVlwoxVasaMeJk3berS+f3ZlzpXS710CVvVv5a2u4tM7v7RfHlpuD6GJ9wr/AAndJnpIWuj2PkXObsfUDSvbh3mjHc8trI6W5+OGERtfJ8MjHejJAe4PyPkfmtmtZunHijua1G9jUlwy2LXREWkbwREQBdWqultoniOsr6eBzvISSBpP71gM7zq14Za5qqrqYo5I4zITI7TYm/fcfl8h6rVq4e09gVRc5TP+mKkveeqpFM3od38wC8O1+X5LboWrrLieyNO4u40Xwrdm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>