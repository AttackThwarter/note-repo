[![FA مشاهده نسخه فارسی](https://img.shields.io/badge/-%D9%85%D8%B4%D8%A7%D9%87%D8%AF%D9%87%20%D9%86%D8%B3%D8%AE%D9%87%20%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-8A2BE2?style=for-the-badge&logo=googletranslate&logoColor=white)](README_fa.md)


# Design and Implementation of an Intelligent System for Extraction and Analysis of Instagram Reels Content Using the N8N Automation Platform

### 1. Project Overview

This project describes an n8n Workflow designed to extract Reels data from specified Instagram profiles. The extracted data is then stored in a Google Sheet for further analysis. This workflow is triggered manually and, for each profile listed in the input Google Sheet, collects the Reels information.

You can also configure it to, for example, collect data weekly and save it to Google Sheets.

---

### 2. Objectives

- Automate the process of collecting Instagram Reels data from a specified list of content creators.
- Extract key metrics such as view count, likes, comments, and other metadata for each Reel.
- Store structured data in Google Sheets for easy access and analysis.

---

### 3. Prerequisites

- An active instance of n8n  
- Access to an Apify account with a valid API Token  
- A Google account with access to the Google Sheets API  
- A Google Sheet with two sheets:  
  - Input sheet (`creators`): containing the column `instagram username`  
  - Output sheet (`videos`): for storing the extracted information  

---

### 4. Workflow Description

1. **Trigger Manual:** Manual start (can be switched to a time trigger, e.g., weekly)  
2. **Google Sheets (CREATOR NAME):** Read usernames  
3. **Loop Over Items (SplitInBatches):** Process users one by one  
4. **Request HTTP:** Send request to Apify  
5. **Time & Date:** Get current date and time (Tehran/Asia timezone)  
6. **Merge:** Merge received data with the timestamp  
7. **Set (Fields Edit):** Select and format fields  
8. **Sort:** Sort by `videoPlayCount`  
9. **Google Sheets (VIDEOS):** Save to Google Sheet  
10. **Wait:** 15-second delay between iterations  

---

### 5. Node Configuration

- By importing the file [instaScraper.json](./instaScraper.json) in this repository, node settings will be applied.

---

### 6. Data Structure

Sample output fields:  
- `id`  
- `type`  
- `caption`  
- `hashtags`  
- `mentions`  
- `url`  
- `commentsCount`  
- `likesCount`  
- `videoPlayCount`  
- `timestamp`  
- `displayUrl`  
- `videoUrl`  
- `ownerUsername`  
- `videoDuration`  
- `currentDate`  

---

### 7. Considerations

- Respect API rate limits  
- Review Apify and Instagram Terms of Service  

# Workflow Diagram

![workFlow](src/image_2025-06-09_18-50-15.png)
