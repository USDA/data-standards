---
layout: page
title: Acreage Crop Reporting About
permalink: /data-elements/business_rules.html
---

<span></span>
**ACRSI Business Rules**
<table class="table table-striped">
			<thead>
				<tr>
					<th>Data Element</th>
					<th>Source</th>
					<th>Obligation</th>
				</tr>
			</thead>
        {% for data_element in site.data.acrsi-data-elements.data_elements %}
        
           {% if data_element.business_rules %}
              {% for business_rule in data_element.business_rules %}
                <tr>
                    <td><a href="{{ data_element.page_name }}.html">{{ data_element.name }}</a></td>
                    <td>{{ business_rule.source }}</td>
                    <td>{{ business_rule.description}}</td>
                </tr>
              {% endfor %}
           {% endif %}

	   {% endfor %}
</table>
