## 
##    Download and install MongoDB client 4.0.6 for Atlas on AWS Cloud9
##    wget -q https://git.io/fjzf1 -O /tmp/setupmongodb.sh && source /tmp/setupmongodb.sh


#   Connect to the Mongo Database on Atlas
#       NOTE: REPLACE THE `<dbuser>` & `<dbname>` WITH YOUR OWN PERSONAL
#           VALUES (WITHOUT THE ANGULAR BRACKETS)

##
##   mongo "mongodb+srv://myfirstcluster-fsmjm.mongodb.net/<db.name>" --username <db.user>
##

##      To Run MONGOshell commands via PYTHON.py script
##          sudo pip3 install dnspython
##          sudo pip3 install pymongo

##      cd.. (in terminal) ---> to home/ubuntu(DIR) and edit (.bashrc)  <--- in home/ubuntu(DIR)
##      nano .bashrc <--- export MONGO_URI="{mogo+svr}"
##      {mongo+svr}  ==
##      mongodb+srv://root:<password>@mac-cluster-4za3h.mongodb.net/test?retryWrites=true&w=majority

##      export MONGO_URI="mongodb+srv://root:<password>@mac-cluster-4za3h.mongodb.net/macTestDB?retryWrites=true&w=majority"


##   MONGOshellCommands
##
##      cls                -clear the screen
##      shocw collections   -displays DB
##      new                -new

##      macTestDB.macDB = coll;

##      --find specif
##      coll.find({gender:"f", nationality:"american"});

##      --find ( or: )
##      coll.find({gender:"f", $or: [{nationality:"american"},{nationality:"irish"}] });

##      --find ( or: ).sort( {name:1} ); --assending 
##               (-1) -- desending
##      coll.find({gender:"f", $or: [{nationality:"american"},{nationality:"irish"}] });


##      --find first and update field
##      coll.update( {nationality:'hispanic'}, { $set: {last:'MIDIpro'}});

##      --find all and update field
##      coll.update( {nationality:'irish'}, { $set: {hair_colour:'red-PURPLE'}}, {multi:true} );

##      --delete obj
##      coll.remove( {first:'student', last:'test'} );

##      --deleteALL 
##      coll.remove();




coll.update(
            {nationality:'irish'},
            { $set: 
                {hair_colour:'red-PURPLE'}
            },
            {multi:true}
        );





