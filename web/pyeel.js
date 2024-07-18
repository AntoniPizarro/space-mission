document.getElementById("stage-planning").addEventListener("click", viewMenuStagePlanning);

async function viewMenuStagePlanning() {
    let stagePlanning = await eel.view_menu_stage_planning()();
    alert(stagePlanning);
}