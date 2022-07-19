function generator() {   
    const path_name = window.location.pathname
    const delta_check = document.getElementById("deltacheck").checked;
    document.getElementById('run_test_button').style.display = "inline";
    const entire_line = area.value.split("\n");
    line_to_run=entire_line; //saving a global copy of entire_line
    const lineNo = textarea_data.value.substr(0, textarea_data.selectionStart).split("\n").length;
    const selText = target; // current target
    if (selText.length == 0) {
        return "";
    } // to avoid undefined when no selection and hit generate
    const lineStart = area.value.lastIndexOf("\n", area.selectionStart) + 1;
    let pre_space="";
    let post_space="";
    // below cond if target-1 is " " 
    if (entire_line[0].charAt(start_target_at-1) === " ")
    {
        pre_space = true;
    } 
    else {
        pre_space = false;
    }
    // below cond if target+1 is " " 
    if (entire_line[0].charAt(end_target_at+1) === " ")
    {
        post_space = true;
    } 
    else {
        post_space = false;
    }
    var entry = {
        grep:wrapper,
        NonGreedy:isgreedychecked,
        URLpath:path_name,
        delta_check: delta_check,
        STATIC_STRINGS: sorted_custom_brd,
        pre_char_space: pre_space,
        post_char_space: post_space,
        LINENUMBER: lineNo,
        TEXTSELECTED: selText,
        start_index: start_target_at,
        end_index: end_target_at,
        TheLineNumStat: islinechecked,
        TheLHSNumStat: isLHSchecked,
        TheRHSNumStat: isRHSchecked,
        full_line: entire_line,
        // word_index:word_index,
        // static_array: custom_brd_list
    }
    //using fetch function to send data to /entry endpoint


    void async function() {

        const response = await fetch(`${window.origin}/entry`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(entry),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        });
        const data = await response.json();
        document.querySelector("#patt1").innerText = data.pattern_1_result;
        document.querySelector("#patt2").innerText = data.pattern_2_result;
        document.querySelector("#patt3").innerText = data.pattern_3_result;
        document.querySelector("#patt4").innerText = data.pattern_4_result;
        document.querySelector("#patt5").innerText = data.pattern_5_result;
        document.querySelector("#patt6").innerText = data.pattern_6_result;
        patt1_run_res = data.pattern_1_result;
        patt2_run_res = data.pattern_2_result;
        patt3_run_res = data.pattern_3_result;
        patt4_run_res = data.pattern_4_result;
        patt5_run_res = data.pattern_5_result;
        patt6_run_res = data.pattern_6_result;
        // document.body.appendChild(document.createTextNode(data.sub_with_spec_nums));
    }();

};