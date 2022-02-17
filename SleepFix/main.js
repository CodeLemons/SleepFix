const electron = require('electron');
const url = require('url');
const path = require('path');

const {app, BrowserWindow, Menu} = electron;

var mainWindow = null;

app.on(
    "window-all-closed",
    function()
    {
        // if ( process.platform != "darwin" )
        {
            app.quit();
        }
    }
);


// Listen for app to be ready
app.on('ready', 
function()
{
    // create window
    var subpy = require( "child_process" ).spawn( "python", [ "./main.py" ] );
    var rp = require( "request-promise" );

    var OpenWindow = function()
    {
        mainWindow = new BrowserWindow( { width: 800, height: 600 } );
        // mainWindow.loadURL( "file://" + __dirname + "/index.html" );
        mainWindow.loadURL(url.format({
            pathname: path.join(__dirname, 'mainWindow.html'),
            protocol:'file',
            slashes: true
        }));
        mainWindow.webContents.openDevTools();
        mainWindow.on(
            "closed",
            function()
            {
                mainWindow = null;
                subpy.kill( "SIGINT" );
            }
        );
    };

    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    Menu.setApplicationMenu(mainMenu);
});

    var StartUp = function()
    {
        rp( mainAddr )
        .then(
            function( htmlString )
            {
                console.log( "server started!" );
                OpenWindow();
            }
        )
        .catch(
            function( err )
            {
                console.log( "waiting for the server start..." );
                // without tail call optimization this is a potential stack overflow
                StartUp();
            }
        );
    };

    StartUp();
const mainMenuTemplate = [
    {
        label:'File',
        submenu:[
            {
                label: 'Quit',
                click(){
                    app.quit();
                }
            }
        ]
    }
];