function run_sed_live() {
    console.log(wrapper);
    if (wrapper===true) {
        alert("sorry, not ready for grep");
        return ""
    }
    document.getElementById('run_test_live').style.display = "inline";
        
        void async function() {
        const response = await fetch(`${window.origin}/run_sed`, {
            method: "GET",
            credentials: "include",
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        });
        const data = await response.json();
        document.getElementById("200").innerText = ">> "+data.patt1_shell_op;
        document.getElementById("201").innerText = ">> "+data.patt2_shell_op;
        document.getElementById("202").innerText = ">> "+data.patt3_shell_op;
        document.getElementById("203").innerText = ">> "+data.patt4_shell_op;
        document.getElementById("204").innerText = ">> "+data.patt5_shell_op;
        document.getElementById("205").innerText = ">> "+data.patt6_shell_op;
        }();
};