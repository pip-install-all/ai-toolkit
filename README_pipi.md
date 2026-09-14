 ### To Get Latest Updates from Original Repo:                                                                       
                                                                                                                     
 ```bash                                                                                                             
   # Always run these two commands together:                                                                         
   git fetch upstream main      # Download latest changes (doesn't modify your work)                                 
   git merge upstream/main      # Apply them to your current branch                                                  
 ```                                                                                                                 
                                                                                                                     
 ### If You Have Changes on Your Branch and Want to Sync:                                                            
                                                                                                                     
 Sometimes you need to rebase instead of merge:                                                                      
                                                                                                                     
 ```bash                                                                                                             
   # Option 1: Merge (creates a merge commit, preserves history as-is)                                               
   git fetch upstream main                                                                                           
   git merge upstream/main                                                                                           
                                                                                                                     
   # Option 2: Rebase (rewrites your commits on top of latest upstream)                                              
   git fetch upstream main                                                                                           
   git rebase upstream/main                                                                                          
 ```                                                                                                                 
                                                                                                                     
 ### To Push Your Changes to YOUR Fork:                                                                              
                                                                                                                     
 ```bash                                                                                                             
   # From your working branch (ai_toolkit_pipi)                                                                      
   git add .                                                                                                         
   git commit -m "Your message"                                                                                      
   git push origin ai_toolkit_pipi  # Pushes to your fork on GitHub                                                  
 ```                                                                                                                 
                                                                                                                     
 ────────────────────────────────────────────────────────────────────────────────                                    
                                                                                                                     
 Quick Reference Commands                                                                                            
                                                                                                                     
 ┌───────────────────────────────────┬────────────────────────────────────────────────────┐                          
 │ Goal                              │ Command                                            │                          
 ├───────────────────────────────────┼────────────────────────────────────────────────────┤                          
 │ Update from original repo         │ git fetch upstream main && git merge upstream/main │                          
 ├───────────────────────────────────┼────────────────────────────────────────────────────┤                          
 │ See what changed between versions │ git log HEAD..upstream/main --oneline              │                          
 ├───────────────────────────────────┼────────────────────────────────────────────────────┤                          
 │ Check your remotes                │ git remote -v                                      │                          
 ├───────────────────────────────────┼────────────────────────────────────────────────────┤                          
 │ Check branches                    │ git branch -a                                      │                          
 └───────────────────────────────────┴────────────────────────────────────────────────────┘     