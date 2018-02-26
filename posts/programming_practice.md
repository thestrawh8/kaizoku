
.. title: Programming Trajectory
.. slug: 
.. date: 2018-02-06 16:06 
.. tags: Programming, Practice
.. category: Solutions
.. link: 
.. description: 
.. type: text


### Merge Two Binary Trees

```c++
class Solution {
public:
    TreeNode* mergeTrees(TreeNode *t1,TreeNode *t2) {
        
        if(t1==NULL && t2==NULL){
            return NULL;
        }
        else{
            if(t1==NULL){
                t1 = t2;
            }
            else if(t1 !=NULL && t2 !=NULL){
                t1->val = t1->val + t2->val;
                t1->left = mergeTrees(t1->left,t2->left);
                t1->right = mergeTrees(t1->right,t2->right);
            }
            return t1;
            }
        }
        
};
```
<!-- TEASER_END -->
### Reverse words in a String

Learned about input stringstream have to check soem more regarding stringstream operation.

```c++
class Solution {
public:
    string reverseWords(string s) {
        std::istringstream tmp(s);
        std::stringstream ss;
        std::vector<std::string> collection((std::istream_iterator<std::string>(tmp)),std::istream_iterator<std::string>());
        for (std::vector<std::string>::iterator it=collection.begin();it!=collection.end();it++){
            std::reverse((*it).begin(),(*it).end());
            ss << *it << " ";  
        }
    std::string result = ss.str();
    result.pop_back();
    return result;
    }
};
```

### Encode and Decode TinyURL

Learned about find operation in unordered::map container it returns an `const_iterator` which points to the given key. If the map doesn't have the key then it will return `map.end()`.

```c++
class Solution {
public:
    std::unordered_map<std::string,std::string> urlencodebuck;
    std::unordered_map<std::string,std::string> urldecodebuck;
    std::string alphanum = "abcdefghijklmnopqrstuvwxyz0123456789";
    std::unordered_map<std::string,std::string>::const_iterator check;

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        check = urlencodebuck.find(longUrl);
        if(check != urlencodebuck.end())
            return urlencodebuck[longUrl];
        else{
            std::string shortUrl = "";
            for(int i=0;i<6;i++){
                shortUrl = shortUrl + alphanum[(rand() % 36)];
            }
            urlencodebuck[longUrl] = shortUrl;
            urldecodebuck[shortUrl] = longUrl;
            return urlencodebuck[longUrl];
        }
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return urldecodebuck[shortUrl];
    }
};
```

> Project Euler

### Multiples of 3 & 5 below 1000

Time taken: 0.00006s

```c++
#include <iostream>
#include <time.h>

int main(){
    clock_t tStart = clock();
    int multiple_3=0,multiple_5=0,multiple_15=0,i=0,sum=0;
    while(multiple_5 <1000){
        sum = sum + multiple_3 + multiple_5;
        multiple_3 = multiple_3 + 3;
        multiple_5 = multiple_5 + 5;
        // multiple_5 = Multiple5(multiple_5);
    }

    while(multiple_3<1000){
        sum = sum + multiple_3;
        multiple_3 = multiple_3 + 3;
    }
    while(multiple_15<1000){
        sum = sum - multiple_15;
        multiple_15 = multiple_15 + 15;
    }
    std::cout << sum << '\n';
    printf("Time taken: %.5fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
} 
```

### My submission

Time taken: 0.00007s

```c++
#include <iostream>
#include <time.h>


int Multiple5(int multiple_5){
    if (multiple_5%3==0){
        multiple_5 = multiple_5 + 5;
        Multiple5(multiple_5);
    }
    else
        return multiple_5;
    
}

int main(){
    clock_t tStart = clock();
    int multiple_3=0,multiple_5=0,multiple_15=0,i=0,sum=0;
    while(multiple_5 <1000){
        sum = sum + multiple_3 + multiple_5;
        multiple_3 = multiple_3 + 3;
        multiple_5 = multiple_5 + 5;
        multiple_5 = Multiple5(multiple_5);
    }

    while(multiple_3<1000){
        sum = sum + multiple_3;
        multiple_3 = multiple_3 + 3;
    }

    std::cout << sum << '\n';
    printf("Time taken: %.5fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
```
