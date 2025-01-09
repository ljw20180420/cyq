const jsdom = require("jsdom");
const { JSDOM } = jsdom;

let geneIDs = [10664];

(async () => {
    for (let geneID of geneIDs) {
        let respone = await fetch('https://www.ncbi.nlm.nih.gov/gene/10664');
        let result = await respone.text();
        const dom = new JSDOM(result)
        const summaryDl = dom.window.document.getElementById('summaryDl')
        console.log(summaryDl.children[19].innerHTML)
    }
})()



