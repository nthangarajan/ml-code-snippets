from utils.format_dict import FormatDict
from llm.google import gemini_flash

from prompts.log_analysis import prompt_report_generation

from state.log_analyser_state import LogAnalyserState

def handle_report_generator(state:LogAnalyserState):
    print("----------------------------------------")
    print("**report_generator** working...")
    pipeline_run_name = state.get('pipeline_run_name', '').strip()
    report_generation = f"pipeline_run_name : {pipeline_run_name}" + "\n"
    
    custom_job_id_list = state.get('custom_job_id_list',[])
    final_result=''
    if len(custom_job_id_list) == 0:
        report_generation = report_generation + 'No Custom Jobs Identified for Pipeline' + "\n"
    else: 
        failure_analysis_reports = state['failure_analysis_report']
        print(len(failure_analysis_reports))
        
        if len(failure_analysis_reports) == 0:
            report_generation = report_generation + ",".join(custom_job_id_list) + "\n"
            report_generation = report_generation + 'No Issues from Custom Jobs' + "\n"
        else:
            for failure_analysis_report in failure_analysis_reports:
                # job_id = failure_analysis.job_id
                # issues = failure_analysis.issues
                exceptions = failure_analysis_report.exceptions
                report_generation = report_generation + "----------------------------------------------" + "\n"
                report_generation = report_generation + "-----------------**job_id**-----------------------" + "\n"
                report_generation = report_generation + f"job_id : {failure_analysis_report.job_id}" + "\n"

                report_generation = report_generation + "-----------------**log_issues**-----------------------" + "\n"
                report_generation  = report_generation + str(failure_analysis_report.issues) +  "\n"
                report_generation = report_generation + "-----------------**exception_info**-----------------------" + "\n"
                report_generation  = report_generation + exceptions + "\n"
                report_generation = report_generation + "----------------------------------------------" + "\n"

                # print("---**input**--:")
                prompt = prompt_report_generation.format_map(FormatDict(log_issues=report_generation)
                                                    )
                final_result = gemini_flash.invoke(prompt).content
                final_result = final_result.strip()

    print("---**response**--:")
    
    return {'report_generation':final_result}


# def handle_report_generator(state:LogAnalyserState):
#     print("----------------------------------------")
#     print("**report_generator** working...")
#     pipeline_run_name = state.get('pipeline_run_name', '').strip()
#     report_generation = f"pipeline_run_name : {pipeline_run_name}" + "\n"
    
#     custom_job_id_list = state.get('custom_job_id_list',[])
    
#     if len(custom_job_id_list) == 0:
#         report_generation = report_generation + 'No Custom Jobs Identified for Pipeline' + "\n"
#     else: 
#         failure_analysis_report_list = state.get('issues')
#         print(len(failure_analysis_report_list))
        
#         if len(failure_analysis_report_list) == 0:
#             report_generation = report_generation + ",".join(custom_job_id_list) + "\n"
#             report_generation = report_generation + 'No Issues from Custom Jobs' + "\n"
#         else:
#             for failure_analysis in failure_analysis_report_list:
#                 job_id = failure_analysis.job_id
#                 issues = failure_analysis.issues
#                 exceptions = failure_analysis.exceptions

#                 report_generation = report_generation + f"job_id : {job_id}" + "\n"

#                 report_generation = report_generation + "-----------------log_issues-----------------------" + "\n"
#                 report_generation  = report_generation + str(issues) +  "\n"
#                 report_generation = report_generation + "-----------------exception_info-----------------------" + "\n"
#                 report_generation  = report_generation + exceptions + "\n"

#     print("---**response**--:")
#     return {'report_generation':report_generation}