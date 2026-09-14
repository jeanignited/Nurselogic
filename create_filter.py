import os

filter_dir = 'src/main/java/com/nurselogic/filter'
if not os.path.exists(filter_dir):
    os.makedirs(filter_dir)

filter_code = '''package com.nurselogic.filter;

import jakarta.servlet.*;
import jakarta.servlet.annotation.WebFilter;
import java.io.IOException;

@WebFilter("/*")
public class CharacterEncodingFilter implements Filter {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        request.setCharacterEncoding("UTF-8");
        response.setCharacterEncoding("UTF-8");
        chain.doFilter(request, response);
    }
}'''

with open(os.path.join(filter_dir, 'CharacterEncodingFilter.java'), 'w', encoding='utf-8') as f:
    f.write(filter_code)
