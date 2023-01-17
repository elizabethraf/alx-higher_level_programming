 #!/usr/bin/node

const request = require('request-promise-native');

const url = `https://swapi-api.alx-tools.com/api/films/`;
const characterId = 18;

async function getMovies(){
    try{
        const data = await request(url,{json: true});
        let count = 0;
        data.forEach(function(item) {
            if(item.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)){
                count++;
            }
        });
        console.log(`Wedge Antilles appeared in ${count} movies`);
    }catch(e){
        console.log(e);
    }
}
getMovies();

