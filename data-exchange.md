---
layout: page
title: Data Exchange

---

These are the __proposed__ data elements for Acreage Reporting to USDA.  No production development
should currently be done based on standards here.  For more information, please see [roadmap](roadmap.html) or provide [feedback](contribute.html).

**Quick Jumps**  

*  [Acreage Crop Reporting Business Case Documentation](about-acrsi.html)  
*  [Proposed XML Schema](https://github.com/bbrotsos/data-standards/tree/master/ag-acrsi.iepd)  
*  [Proposed JSON Schema](https://github.com/bbrotsos/data-standards/tree/master/json-schema)  
*  [Examples](https://github.com/bbrotsos/data-standards/tree/master/examples)  
*  [Acreage Crop Reporting Business Rules](data-elements/business_rules.html) 
*  [XML - JSON Mappings](#xml_json) 



<h2>About ACRSI</h2>
Acreage Crop Reporting Streamlining Initiative (ACRSI) officially started in July 2010. By streamlining and 
automating reporting, ACRSI will reduce the burden on the producer to participate in USDA programs while 
simultaneously improving program integrity and data sharing across USDA agencies and programs. 
Ultimately, ACRSI will allow automated reporting from the producer’s precision farming equipment or 
farm management system.  

![Logical Model](assets/img/logical_model.png)


<h2>Purpose</h2>
This document represents a readable form for the metadata for the entities and attributes included in the 
Logical Data Model for the ACRSI acreage report transmission.

<h3>Common Acreage Reporting Transmission (CART)</h3>

This file is used to transmit an acreage report from an FSA County Office, an Approved Insurance Provider 
(AIP), or a producer to the Common Information Management System (CIMS) Clearinghouse.    

<h4>1.3.1	Specifications</h4>
The CART file is a JavaScript Object Notation (JSON) formatted file with optional embedded GeoJSON 
elements for spatial components. JSON standards can be found at
 https://google-styleguide.googlecode.com/svn/trunk/jsoncstyleguide.xml or more generally at json.org. 
 GeoJSON standards can be found at http://geojson.org/geojson-spec.html. 
 Currently, only polygons, including “inclusion” polygons (sometimes called ‘donuts’) are accepted.  


<a name="xml_json"/>

**XML/JSON Mapping**
<table class="table table-striped">
   <thead>
      <tr>
          <th>Element Name</th>
          <th>XML Name</th>
          <th>JSON Name</th>
      </tr>
    </thead>
    {% for data_element in site.data.acrsi-data-elements.data_elements %}
        <tr>
				<td><a href="data-elements/{{ data_element.page_name }}.html">{{ data_element.name }}</a></td>
				<td>
					{{ data_element.xml_name }}
				</td>
				<td>{{ data_element.json_name}}</td>
		</tr>
		{% endfor %}
</table>
    
    




