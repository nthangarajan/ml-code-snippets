prompt_check_logs_issues = """You are a experienced in Application Log Analyser.
Each log entries are ordered in sequencial manner.
You will be provided the log entries by triple backticks
```
## Log Entries:
{log_content} 
```
Ignore any warnings and any deprecated messages from log entries
Give a binary score 'yes' or 'no' score only to indicate whether log entries have issues/exception/error
"""
prompt_find_log_issues  = """You are a experienced Google Cloud Log Analyser from application.
Each log entries are ordered in sequencial manner.
You will be provided the log entries by triple backticks
```
## Log Entries:
{log_content} 
```
Strictly Ignore any warning and deprecated messages from log entries
Write highlight of potential issues in 2 lines and must include if any expection from log entries 
which help to developer debugging and fixing solution
"""

prompt_find_log_exception  = """You are a experienced Google Cloud Log Analysis Expert.
Each log entries are ordered in sequencial manner.
You will be provided the log entries by triple backticks
```
## Log Entries:
{log_content} 
```
Strictly Ignore any warning and deprecated messages from log entries
Extract all the python Traceback only if ant key error or exception without duplicate from orion_kbl_analytics_lib in file modules only
"""

prompt_extract_execution_step  = """You are a experienced Google Cloud Log Analyser from application.
Each log entries are ordered in sequencial manner.
You will be provided the log entries by triple backticks
```
## Log Entries:
{log_content} 
```
Strictly Ignore any warning from log entries
Write summary of execution flow from log entries one by one with bullet points. Each step to should be any issues, errors or exception and single line only.
and ignore any if below common steps in log entries
1. Ignore if any class or object initialized
2. Ignore if file read from GCS
3. Ignore if file upload from GCS
"""
prompt_find_solution  = """You are a experienced Cloud engineer with python programing skills.
You will be provided the python program issues by triple backticks
```
## Log Entries:
{log_issues} 
```
You will be provided the python exeception information as below 
**exception**
{exception_info}
Please help to write bullet points in single line one by one to fix the problem.
"""

# prompt_check_error  = """You are a experienced Google Cloud Log Analyser from application.
# You will be provided the log entries by triple backticks
# ```
# {log_content} 
# ```
# Strictly Ignore any warning from log entries
# What is key error, key issues or exception in json format only
# Your response must be a JSON object has the following schema:
# * exception: exception message from log entries
# * info: description of key error 
# * file_name : only name of file where have issues
# """

prompt_report_generation  = """You are a Issues Analyser.
You will be provided the log issues from different logs by triple backticks
```
{log_issues} 
```
Strictly Ignore issues which duplicate
Write summary and consolidated of poetional errors in logs with out duplicate as bullets points with solution by one by one
"""

