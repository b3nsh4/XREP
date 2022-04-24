function run_sed_live() {
    document.getElementById('run_test_live').style.display = "inline";
    total_patterns = {
        patt1: patt1_run_res,
        patt2: patt2_run_res,
        patt3: patt3_run_res,
        patt4: patt4_run_res,
        patt5: patt5_run_res,
        patt6: patt6_run_res,
        full_line: line_to_run
    }
        
        void async function() {
        const response = await fetch(`${window.origin}/run_test`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(total_patterns),
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