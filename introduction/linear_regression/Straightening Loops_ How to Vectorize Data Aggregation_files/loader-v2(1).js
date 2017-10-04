(function() {

    var __hs_cta_json = {"css":"a#cta_button_532045_4e0d2014-a652-446c-b385-da9d9219ba70 {\n  cursor:pointer !important; \n}\na#cta_button_532045_4e0d2014-a652-446c-b385-da9d9219ba70:hover {\n}\na#cta_button_532045_4e0d2014-a652-446c-b385-da9d9219ba70:active, #cta_button_532045_4e0d2014-a652-446c-b385-da9d9219ba70:active:hover {\n}\n\n","image_html":"<a id=\"cta_button_532045_4e0d2014-a652-446c-b385-da9d9219ba70\" class=\"cta_button\" href=\"https://cta-service-cms2.hubspot.com/ctas/v2/public/cs/c/?cta_guid=4e0d2014-a652-446c-b385-da9d9219ba70&placement_guid=74a4e9d5-d6c1-4dc1-b494-9f4c45847000&portal_id=532045&redirect_url=APefjpE7b5qzBtnFGpcOgXA9_LG2TFMLk69QfLrF72h91RYjv3sqAlaVDei2uR6-kozrOq-8eTQXNciKu0f4dfqIOLmvADKHZ_r3YRJ8ttPrgPlO2WyBvlUGX0UoADguOOwRKdMgSJZR&hsutk=c7a00000158612ca12f8015ecc7e1cbb&canon=https%3A%2F%2Fwww.datascience.com%2Fblog%2Fstraightening-loops-how-to-vectorize-data-aggregation-with-pandas-and-numpy%2F&click=83cb9be9-3dd6-4731-b9f8-3795bae3cef2&utm_referrer=https%3A%2F%2Fmubaris.com%2F2017-09-28%2Flinear-regression-from-scratch&pageId=3875087619\"  cta_dest_link=\"https://www.datascience.com/request-demo\"><img id=\"hs-cta-img-74a4e9d5-d6c1-4dc1-b494-9f4c45847000\" class=\"hs-cta-img \" style=\"border-width: 0px; /*hs-extra-styles*/\" mce_noresize=\"1\" alt=\"Request Demo\" src=\"https://cdn2.hubspot.net/hubshot/16/09/09/9da3094e-ecbc-45ea-8cd3-7aa723ada96e.png\" /></a>","is_image":false,"placement_element_class":"hs-cta-74a4e9d5-d6c1-4dc1-b494-9f4c45847000","raw_html":"<a id=\"cta_button_532045_4e0d2014-a652-446c-b385-da9d9219ba70\" class=\"cta_button \" href=\"https://cta-service-cms2.hubspot.com/ctas/v2/public/cs/c/?cta_guid=4e0d2014-a652-446c-b385-da9d9219ba70&placement_guid=74a4e9d5-d6c1-4dc1-b494-9f4c45847000&portal_id=532045&redirect_url=APefjpE7b5qzBtnFGpcOgXA9_LG2TFMLk69QfLrF72h91RYjv3sqAlaVDei2uR6-kozrOq-8eTQXNciKu0f4dfqIOLmvADKHZ_r3YRJ8ttPrgPlO2WyBvlUGX0UoADguOOwRKdMgSJZR&hsutk=c7a00000158612ca12f8015ecc7e1cbb&canon=https%3A%2F%2Fwww.datascience.com%2Fblog%2Fstraightening-loops-how-to-vectorize-data-aggregation-with-pandas-and-numpy%2F&click=83cb9be9-3dd6-4731-b9f8-3795bae3cef2&utm_referrer=https%3A%2F%2Fmubaris.com%2F2017-09-28%2Flinear-regression-from-scratch&pageId=3875087619\"  style=\"/*hs-extra-styles*/\" cta_dest_link=\"https://www.datascience.com/request-demo\" title=\"Request Demo\"><button>Request Demo</button></a>"};
    var __hs_cta = {};

    __hs_cta.drop = function() {
        var is_legacy = document.getElementById('hs-cta-ie-element') && true || false,
            html = __hs_cta_json.image_html,
            tags = __hs_cta.getTags(),
            is_image = __hs_cta_json.is_image,
            parent, _style;

        if (!is_legacy && !is_image) {
            parent = (document.getElementsByTagName("head")[0]||document.getElementsByTagName("body")[0]);

            _style = document.createElement('style');
            parent.insertBefore(_style, parent.childNodes[0]);
            try {
                default_css = ".hs-cta-wrapper p, .hs-cta-wrapper div { margin: 0; padding: 0; }";
                cta_css = default_css + " " + __hs_cta_json.css;
                // http://blog.coderlab.us/2005/09/22/using-the-innertext-property-with-firefox/
                _style[document.all ? 'innerText' : 'textContent'] = cta_css;
            } catch (e) {
                // addressing an ie9 issue
                _style.styleSheet.cssText = cta_css;
            }

            html = __hs_cta_json.raw_html;
        }

        for (var i = 0; i < tags.length; ++i) {

            var tag = tags[i];
            var images = tag.getElementsByTagName('img');
            var cssText = "";
            var align = "";
            for (var j = 0; j < images.length; j++) {
                align = images[j].align;
                images[j].style.border = '';
                images[j].style.display = '';
                cssText = images[j].style.cssText;
            }

            if (align == "right") {
                tag.style.display = "block";
                tag.style.textAlign = "right";
            } else if (align == "middle") {
                tag.style.display = "block";
                tag.style.textAlign = "center";
            }

            tag.innerHTML = html.replace('/*hs-extra-styles*/', cssText);
            tag.style.visibility = 'visible';
            tag.setAttribute('data-hs-drop', 'true');
            window.hbspt && hbspt.cta && hbspt.cta.afterLoad && hbspt.cta.afterLoad('74a4e9d5-d6c1-4dc1-b494-9f4c45847000');
        }

        return tags;
    };

    __hs_cta.getTags = function() {
        var allTags, check, i, divTags, spanTags,
            tags = [];
            if (document.getElementsByClassName) {
                allTags = document.getElementsByClassName(__hs_cta_json.placement_element_class);
                check = function(ele) {
                    return (ele.nodeName == 'DIV' || ele.nodeName == 'SPAN') && (!ele.getAttribute('data-hs-drop'));
                };
            } else {
                allTags = [];
                divTags = document.getElementsByTagName("div");
                spanTags = document.getElementsByTagName("span");
                for (i = 0; i < spanTags.length; i++) {
                    allTags.push(spanTags[i]);
                }
                for (i = 0; i < divTags.length; i++) {
                    allTags.push(divTags[i]);
                }

                check = function(ele) {
                    return (ele.className.indexOf(__hs_cta_json.placement_element_class) > -1) && (!ele.getAttribute('data-hs-drop'));
                };
            }
            for (i = 0; i < allTags.length; ++i) {
                if (check(allTags[i])) {
                    tags.push(allTags[i]);
                }
            }
        return tags;
    };

    // need to do a slight timeout so IE has time to react
    setTimeout(__hs_cta.drop, 10);

}());
