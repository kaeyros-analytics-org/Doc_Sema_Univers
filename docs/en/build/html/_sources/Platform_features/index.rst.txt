Overview
=========

The attendance platform developed by **Kaeyros Analytics** allows clients to ensure two main functions:

* **Manage attendance** and users within their own company;
* **Distribute and administer the solution** on behalf of other client organizations (for customers with **Reseller** status).

This section details the different usage steps, starting with logging into the administration platform.

Logging into the Administration Platform
=====================================================

Access to the administration platform is done via a web browser. Here are the steps to log in:

1. **Open your browser** (Google Chrome, Firefox, Edge, etc.)
2. Enter the following URL: `https://pointing-front.kaeyros.org`
3. Enter the **credentials provided** during the subscription to the **service** (email address and password)
4. Click **"Login"** to access your account.

.. image:: ../images/image1.png

If you forget your password, please contact us to obtain a new one. Once logged in, you will be redirected to the reporting dashboard, where you can view employees’ attendance data for a given day.

.. image:: ../images/image2.png

Reporting Dashboard
====================================

Once connected to the dashboard, you can view daily attendance, manually enter attendance, download the attendance report, and consult global reporting.

**i. Navigating between days**
Navigation between days is done using the following two buttons:

.. image:: ../images/image3.png

Clicking the **<** button takes you to the previous day; clicking the **>** button takes you to the next day.

**ii. Manually entering attendance**
This function is intended for authorized personnel (e.g., reception staff) to manually record an employee’s attendance.

1. Click on the **Enter attendance** button.

   .. image:: ../images/image4.png

2. A dialog box opens: select the employee concerned as well as their site.

   .. image:: ../images/image5.png

3. Click **Validate** to save the attendance.

Once validated, the attendance appears in the day’s summary table.

**Important**: each employee must clock in **twice a day**:

* **Clock In**: arrival time
* **Clock Out**: departure time.

**iii. Downloading the daily attendance report**

1. Navigate to the day for which you want to generate a report.
2. Click the **Attendance Report** button.

   .. image:: ../images/image6.png

3. An Excel file containing all employees’ attendance for the selected day is automatically downloaded.

   .. image:: ../images/image7.png

**File structure**:

* **Employee**: employee’s name
* **Arrival / Departure**: check-in/out times
* **Site**: location of the attendance
* **Delay Value**: duration of any delay
* **Overtime**: hours worked beyond the standard
* **Balance**: difference between expected and actual worked time.

**iv. Viewing daily attendance statistics**

.. image:: ../images/image8.png

You can view:

* The number of employees who arrived on time
* The number of late employees
* Attendance, lateness, and punctuality percentages, displayed on the right-hand side of the dashboard.

**v. Viewing attendance details**

.. image:: ../images/image9.png

The displayed data includes the same columns as the Excel report: arrival and departure times, site, delay, overtime, and balance.

You can also use the following options: search by employee name, filter by site, and navigate between pages using the pagination menu.

**vi. Viewing global reporting**
The global reporting feature allows you to analyze employees’ attendance trends over an extended period (month, quarter, year). Unlike the daily dashboard, this view provides a global summary to help evaluate punctuality and attendance at the company or department level.

1. From the **Main Dashboard**, click the **View Global Reporting** link.

   .. image:: ../images/image10.png

2. You will automatically be redirected to the **second Dashboard**, dedicated to global analysis.

   .. image:: ../images/image11.png

3. Select the desired period (**month, quarter, year**) using the available filters.

Configure your platform
=======================================
The initial platform setup is reserved for users with the **Administrator** role. It allows you to define the company’s key structures: **sites, working hours, departments**, and **positions**.

All these options are accessible from the **Settings** tab.

**i. Adding Sites**

1. Go to the **Settings** tab. You are automatically redirected to the **Sites** sub-tab.

   .. image:: ../images/image12.png

2. Click the **Add Site** button.

   .. image:: ../images/image13.png

3. A dialog box opens. Fill in the following information:

   * **Site name**
   * **Phone number** (used for WhatsApp attendance integration)
   * **Site address**
   * **Geographic coordinates** (click **Get Location**, ensuring geolocation is enabled on your device).

     .. image:: ../images/image14.png

4. Click **Next** to define working hours:

   * Select **working days**
   * Indicate **opening and closing hours** (e.g., 08:30 – 17:30).

     .. image:: ../images/image15.png

5. Click **Validate** to finalize.

Once validated, a **QR Code** is automatically generated. This QR Code is used for employees’ attendance at the given site.

.. image:: ../images/image16.png

**Tip**: before printing or sharing, test the QR Code to make sure it redirects correctly to the configured WhatsApp number.

**ii. Viewing and editing a site**

1. Still in the **Sites** sub-tab, view the list of already created sites.

   .. image:: ../images/image17.png

2. To edit or delete a site, click the **Edit** button:

   * You can update the **name**, **phone number**, **geographic coordinates**, and **working hours**
   * You can also **delete** a site if necessary.

3. To download a site’s QR Code, click the **Download** icon next to the Edit button.

**iii. Configuring working hours**

1. Go to the **Working Hours** sub-tab under **Settings**.

2. Select the relevant site from the dropdown list.

   .. image:: ../images/image18.png

3. Adjust the hours as needed (working days, opening/closing hours).

4. Save your changes by clicking **Validate**.

**iv. Configuring departments**

1. Go to the **Department** sub-tab.

   .. image:: ../images/image19.png

2. You can:

   * View the list of existing departments
   * **Edit** a department’s name using the **Edit** button
   * **Delete** a department using the **Edit** button.

**v. Configuring positions**

1. Go to the **Position** sub-tab.

   .. image:: ../images/image20.png

2. You can:

   * View all company positions
   * **Edit** the title or description of a position
   * **Delete** an existing position using the Edit button.

Employee Management
============================

This is done from the **Employee** tab.

.. image:: ../images/image21.png

In this tab, you can view registered employees, add a new employee, edit employee information, or delete an employee.

.. image:: ../images/image22.png

**i. Adding an employee**
By clicking the **Add Employee** button, you can add a new employee. A dialog box opens, and you must enter the employee’s name, phone number, email address, position, and department.

.. image:: ../images/image23.png

⚠️ **Important**: For the phone number, make sure to enter it exactly as it is on WhatsApp (e.g., numbers without 6 like `23789898989`, and numbers with 6 like `237689898989`).

**ii. Viewing, editing, and deleting an employee**
The process is the same as in other cases. Using the **Edit** button, you can choose either to modify or to delete the employee depending on what you want to do.

.. image:: ../images/image24.png

Account Management
=========================

This is done from the **Account** tab. Only users with the role of **Admin** or **Account Manager** can see this tab.

.. image:: ../images/image25.png

This section has two main features: Add a new company and Add a user.

**i. Adding a company**
This feature allows you to create a new company to which you want to sell the attendance tool. You must add the company here and then add a user to manage it.

Clicking the **Add Company** button opens a dialog box where you must fill in the company’s details.

.. image:: ../images/image26.png

.. image:: ../images/image27.png

You must provide the company name, the name of a company representative, email, and phone number, then click **Validate** to complete the company creation. You cannot create two companies with the same phone number.

**ii. Viewing, editing, deleting companies**

.. image:: ../images/image28.png

When you create a new company, it is automatically added to the list of companies, as shown above. Using the Edit button on the far right of each company, you can:

* Edit the company’s information (click **Edit**)
* Delete the company (click **Delete**).

**Note**: If you have the **Account Manager** role, you can only view and edit companies you added yourself. You cannot edit a company created by an Admin or another Account Manager.

**iii. Adding a user**
Generally, when you create a company, you must add a user to manage it and assign them the **Admin** role.

In the **User** sub-tab, click the **Add User** button to start the process.

.. image:: ../images/image29.png

A dialog box opens where you must fill in the user’s details.

.. image:: ../images/image30.png

You are responsible for sending the credentials (email and password) to the user so they can access the platform to manage their company.

**iv. Viewing, editing, deleting users**

.. image:: ../images/image31.png

When you add a new user, they automatically appear in the list, as shown above. Using the Edit button on the far right of each user, you can:

* Modify the user’s information (click **Edit**)
* Delete the user if necessary (click **Delete**).

**Note**: If you have the **Account Manager** role, you can only view and edit users you created yourself. You cannot edit a user added by an Admin or another Account Manager.