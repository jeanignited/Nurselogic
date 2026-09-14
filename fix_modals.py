# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Add the closing div to glasgowContainerAtender
old_str = '''                              </select>
                          </div>
                      </div>
                  </div>
  
                  <!-- Tab Diagnostico y Receta -->'''

new_str = '''                              </select>
                          </div>
                      </div>
                      </div>
                  </div>
  
                  <!-- Tab Diagnostico y Receta -->'''

if old_str in c:
    c = c.replace(old_str, new_str)
    with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Success")
else:
    print("Not found")
