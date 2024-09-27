////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* global mock set */
static bool mock_{function_name} = false;
constexpr int mock_{function_name}_errno = 1;
enum class {function_name}_case_des : int {{
  ret_1,
}};
static {function_name}_case_des {function_name}_case = {function_name}_case_des::ret_1;
/* {function_name} mock set */
typedef {function_return} (*{function_name}_func_t)({function_param});
/* The real function address function */
{function_name}_func_t {function_name}_func = reinterpret_cast<{function_name}_func_t>(dlsym(RTLD_NEXT,"{function_name}"));
/* {function_name} mock */
extern "C" {function_return} {function_name}({function_param}) {{
  if (mock_{function_name}) {{
    if ({function_name}_case == {function_name}_case_des::ret_1) {{
      return {function_return}{{}};
    }} else if ( 1 ) {{
      return {function_return}{{}};
    }} else {{
      return {function_return}{{}};
    }}
  }} else {{
    return {function_name}_func({function_name_list});
  }}
}}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////