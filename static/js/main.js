
let lrhs = "";
let custom_brd_list = []; // dict to store the index , selText
let target = ""; //current target
//below is index range of the target
let lineStart = 0;
let start_target_at = 0;
let end_target_at = 0;
let dynamic_static_id=100;
//above is index range of the target

const textarea_data = document.getElementById("area");

function handle_select() { // this fn is to display the current selected text onselect event 

    var CheckBox_StaticBrd = document.getElementById("brdcheck").checked;
    // displaying target
    lineStart = area.value.lastIndexOf("\n", area.selectionStart) + 1;

    if (CheckBox_StaticBrd == false) { //if static is not checked, it should be target. else its boundary

    target = textarea_data.value.substr(textarea_data.selectionStart, textarea_data.selectionEnd -textarea_data.selectionStart);
        start_target_at = area.selectionStart - lineStart; // t0
        end_target_at = area.selectionEnd - lineStart; // t1
    } // if cond ends
    else if (CheckBox_StaticBrd == true) {
        let start_bndry_at = area.selectionStart - lineStart; // b0
        let end_bndry_at = area.selectionEnd - lineStart; // b1

    }

    if (target.length > 50) { // this is the limit of 50 chars, backend behaves the same.
        document.getElementById("target_text").innerText = "_𝘯𝘰𝘯-𝘶𝘴𝘦𝘧𝘶𝘭 𝘱𝘢𝘵𝘵𝘦𝘳𝘯_";
    } else {
        document.getElementById("target_text").innerText = target;
    }
}

let islinechecked = false;
let isRHSchecked = false;
let isLHSchecked = false;
// add more vars if needed to above

function LineChkFn() {
    islinechecked = document.getElementById("LineChecker").checked;

}

function RHSChkFn() {
    isRHSchecked = document.getElementById("RHSChecker").checked;

}

function LHSChkFn() {
    isLHSchecked = document.getElementById("LHSChecker").checked;

}
// when hit "add" selText will be displayed whereever mentioned

function add_custombrd() {

    if (target == "") {
        return alert("_add 'target' first_"); // if user is choosing boundary before target
    }
    // sorting the custom_brd_list below

    const brd_lineStart = area.value.lastIndexOf("\n", area.selectionStart) + 1;
    const start_bndry_at = area.selectionStart - brd_lineStart; // b0
    const end_bndry_at = area.selectionEnd - brd_lineStart; // b1
    const selText = textarea_data.value.substr(textarea_data.selectionStart, textarea_data.selectionEnd - textarea_data.selectionStart);

    if (start_target_at > end_bndry_at) {
        lrhs = 'lhs';
    } else if (start_bndry_at > end_target_at) {
        lrhs = 'rhs';
    } else {
        alert("Static strings cannot include target itself!");
        return; // if boundary include target itself, yell!!
    }
    

    //making sure to restrict 4 strings
    if (custom_brd_list.length > 3)
    {
        return alert("not more than 4 static strings");
    }
    else{

        push_statics = ({
            index: [start_bndry_at, end_bndry_at],
            word: selText,
            lrhs: lrhs
        });
        custom_brd_list.push(push_statics);
        document.getElementById(dynamic_static_id).innerText = selText;
        dynamic_static_id=dynamic_static_id+1;
        //  check duplicate static strings
        sorted_custom_brd = custom_brd_list.sort((a, b) => {
        if (a.index[0] === b.index[0])
        {   
            clear_static_brd()
            return alert("duplicate static string found! already added!");
        }
        else if (a.index[0] < b.index[0])
        {
        return;
        }
            }); 
        // end check


    }

    // add text to 100 101 102 id
}

function clear_static_brd() {
    document.getElementById("100").innerText="";
    document.getElementById("101").innerText="";
    document.getElementById("102").innerText="";
    document.getElementById("103").innerText="";
    custom_brd_list = []; //clear elements
    dynamic_static_id=100;
       
}

// if staticbrd is checked, show options, else show nothing
function show_brd_options() {
    var CheckBox_StaticBrd = document.getElementById("brdcheck").checked;
    if (CheckBox_StaticBrd == true) {
        document.getElementById('makeclear').style.display = "inline";
        document.getElementById('add_static').style.display = "inline";
		document.getElementById('display_static_brd').style.display = "inline";
    } else {
        document.getElementById('makeclear').style.display = "none";
        document.getElementById('add_static').style.display = "none";
        document.getElementById('display_static_brd').style.display = "none"; 

    }
}

function copyElementText(id) {
    var text = document.getElementById(id).innerText;
    var elem = document.createElement("textarea");
    document.body.appendChild(elem);
    elem.value = text;
    elem.select();
    document.execCommand("copy");
    document.body.removeChild(elem);

}

let sorted_custom_brd=[];

function generator() {        

    const entire_line = area.value.split("\n");
    const lineNo = textarea_data.value.substr(0, textarea_data.selectionStart).split("\n").length;
    const selText = target; // current target
    if (selText.length == 0) {
        return "";
    } // to avoid undefined when no selection and hit generate
    const lineStart = area.value.lastIndexOf("\n", area.selectionStart) + 1;


    var entry = {
        STATIC_STRINGS: sorted_custom_brd,
        LINENUMBER: lineNo,
        TEXTSELECTED: selText,
        WHOLE_STUFF: entire_line,
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

        // document.body.appendChild(document.createTextNode(data.sub_with_spec_nums));
    }();

};