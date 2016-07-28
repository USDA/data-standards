---
layout: page
title: Data Elements
permalink: /data-elements/
---

These are the __proposed__ data elements for Acreage Reporting to USDA.  No production development
should currently be done based on standards here.  For more information, please see [roadmap](../roadmap.html) or provide [feedback](../contribute.html).

*  [Acreage Crop Reporting Business Case Documentation](../about-acrsi.html)  

<span></span>
<table class="table table-striped">
			<thead>
				<tr>
					<th>Element Name</th>
					<th>Description</th>
					<th>Type</th>
				</tr>
			</thead>
        {% for data_element in site.data.acrsi-data-elements.data_elements %}
        <tr>
				<td><a href="{{ data_element.page_name }}.html">{{ data_element.name }}</a></td>
				<td>
					{{ data_element.definition }}
				</td>
				<td>{{ data_element.data_type_code}}</td>
		</tr>
		{% endfor %}
</table>
