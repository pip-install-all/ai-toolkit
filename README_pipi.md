```                                                                                                                 
   ┌─────────────────────────────────────┐                                                                           
   │  UPSTREAM (Original Author's Repo)   │                                                                          
   │         main                        │                                                                           
   └──────────┬──────────────────────────┘                                                                           
              │ fetch updates FROM here                                                                              
              ↓                                                                                                      
   ┌─────────────────────────────────────┐                                                                           
   │  YOUR FORK on GitHub                │                                                                           
   │  ┌───────────────────────────────┐  │                                                                           
   │  │ main                          │  │ ← Clean copy (always matches upstream)                                    
   │  └──────┬───────────────────────┘  │                                                                            
   │         │ branch off here           │                                                                           
   │  ┌──────▼───────────────────────┐  │                                                                            
   │  │ ai_toolkit_pipi             │  │ ← YOUR modifications live HERE                                              
   │  └─────────────────────────────┘  │                                                                             
   └─────────────────────────────────────┘                                                                           
 ```                                                                                                                 
                                                                                                                     
 ────────────────────────────────────────────────────────────────────────────────                                    
                                                                                                                     
 🔄 Daily Workflow: Sync with Upstream (Get Latest Updates)                                                          
                                                                                                                     
 When: Original repo updated, you want fresh code + keep your changes                                                
                                                                                                                     
 ### Step 1: Fetch from Upstream                                                                                     
                                                                                                                     
 ```bash                                                                                                             
   git fetch upstream                                                                                                
 ```                                                                                                                 
                                                                                                                     
 ### Step 2: Update Your Clean main to Match Upstream                                                                
                                                                                                                     
 ```bash                                                                                                             
   git checkout main                                                                                                 
   git reset --hard upstream/main                                                                                    
 ```                                                                                                                 
                                                                                                                     
 ### Step 3: Rebase Your Feature Branch (Bring Your Changes on Top)                                                  
                                                                                                                     
 ```bash                                                                                                             
   git checkout ai_toolkit_pipi                                                                                      
   git rebase main                                                                                                   
 ```                                                                                                                 
                                                                                                                     
 If conflicts occur:                                                                                                 
 1. Edit the conflicted file(s), resolve manually                                                                    
 2. Run: git add <file-name>                                                                                         
 3. Run: git rebase --continue                                                                                       
 4. Repeat until done, then: git rebase --finish                                                                     
                                                                                                                     
 ### Step 4: Push to Your Fork (Optional — if you want GitHub updated)                                               
                                                                                                                     
 ```bash                                                                                                             
   git push origin ai_toolkit_pipi --force-with-lease                                                                
 ```                                                                                                                 
                                                                                                                     
 ────────────────────────────────────────────────────────────────────────────────                                    
                                                                                                                     
 ➕ Add Your New Changes to Feature Branch                                                                           
                                                                                                                     
 When: You've modified files and want them saved in ai_toolkit_pipi                                                  
                                                                                                                     
 ```bash                                                                                                             
   # Make sure you're on feature branch                                                                              
   git checkout ai_toolkit_pipi                                                                                      
                                                                                                                     
   # Stage your changes                                                                                              
   git add <file-name>                                                                                               
   # or: git add .   (stages ALL changes)                                                                            
                                                                                                                     
   # Commit with message                                                                                             
   git commit -m "Description of what you changed"                                                                   
                                                                                                                     
   # Push to GitHub (optional)                                                                                       
   git push origin ai_toolkit_pipi --force-with-lease                                                                
 ```                                                                                                                 
                                                                                                                     
 ────────────────────────────────────────────────────────────────────────────────                                    
                                                                                                                     
 👀 View What's Different Between Branches                                                                           
                                                                                                                     
 See only your modifications:                                                                                        
                                                                                                                     
 ```bash                                                                                                             
   git diff main..ai_toolkit_pipi                                                                                    
 ```                                                                                                                 
                                                                                                                     
 See summary of changed files:                                                                                       
                                                                                                                     
 ```bash                                                                                                             
   git diff main..ai_toolkit_pipi --stat                                                                             
 ```                                                                                                                 
                                                                                                                     
 Check current branch and status:                                                                                    
                                                                                                                     
 ```bash                                                                                                             
   git status                                                                                                        
   git branch                                                                                                        
 ```                                                                                                                 
                                                                                                                     
 ────────────────────────────────────────────────────────────────────────────────                                    
                                                                                                                     
 🧹 Quick Reference: Common Commands                                                                                 
                                                                                                                     
 ┌────────────────────────────────┬──────────────────────────────────────┐                                           
 │ Command                        │ What It Does                         │                                           
 ├────────────────────────────────┼──────────────────────────────────────┤                                           
 │ git fetch upstream             │ Check for updates from original repo │                                           
 ├────────────────────────────────┼──────────────────────────────────────┤                                           
 │ git checkout main              │ Switch to clean copy branch          │                                           
 ├────────────────────────────────┼──────────────────────────────────────┤                                           
 │ git checkout ai_toolkit_pipi   │ Switch to your feature branch        │                                           
 ├────────────────────────────────┼──────────────────────────────────────┤                                           
 │ git reset --hard upstream/main │ Make main match upstream exactly     │                                           
 ├────────────────────────────────┼──────────────────────────────────────┤                                           
 │ git rebase main                │ Move your changes onto updated base  │                                           
 ├────────────────────────────────┼──────────────────────────────────────┤                                           
 │ git add <file>                 │ Stage file for commit                │                                           
 ├────────────────────────────────┼──────────────────────────────────────┤                                           
 │ git commit -m "msg"            │ Save staged changes                  │                                           
 └────────────────────────────────┴──────────────────────────────────────┘                                           
                                                                                                                     
 ────────────────────────────────────────────────────────────────────────────────                                    
                                                                                                                     
 ⚠️ Important Notes                                                                                                  
                                                                                                                     
 1. Your modifications ONLY live in ai_toolkit_pipi — they are NOT copied to main                                    
 2. Main stays clean — always matches upstream, no personal changes                                                  
 3. Rebase reorganizes history — that's why we use --force-with-lease when pushing after rebase (safer than regular  
    force)                                                                                                           
                                                                                                                     
 ────────────────────────────────────────────────────────────────────────────────                                    
                                                                                                                     
 🔍 Verify Setup is Correct                                                                                          
                                                                                                                     
 ```bash                                                                                                             
   # Show your branches and remotes                                                                                  
   git branch -a                                                                                                     
   git remote -v                                                                                                     
                                                                                                                     
   # Confirm main matches upstream                                                                                   
   git log main -1 --oneline                                                                                         
   git log upstream/main -1 --oneline                                                                                
   # Both should show same commit hash if synced                                                                     
 ``` 