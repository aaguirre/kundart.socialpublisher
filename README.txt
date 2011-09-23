Overview
 
Kundart SocialPublisher allows you to publish your content types to Twitter and/or Facebook just by one click.

The purpose of this product is to help Content Managers or Social Community Managers to rapidly publish their content to Social Networks without having to do it manually to each case.

This is NOT a social sharing product. This product is aimed to publish your content to predefined facebook/twitter accounts.

Dependencies
It requires python-twitter to work properly, which installed automatically during the buildout process.

Requirements
Plone 4, but should work on Plone 3 (not tested)

Installation
Just add kundart.socialpublisher to the eggs section of your buildout configuration and run buildout

[buildout]
...
eggs =
    kundart.socialpublisher
Your content type should implement the ISocialPost interface. By default, News Item objects will implement this interface after installing the SocialPublisher product.

   <class class="Products.ATContentTypes.content.newsitem.ATNewsItem">    
        <implements interface="kundart.socialpublisher.interfaces.ISocialPost" />
    </class>     
Configuration
In order to be able to publish to Facebook and Twitter it's necessary to obtain the required tokens and access keys provided by both social networks.

We are not going to explain here about how you can get these tokens but you can read the Facebook and Twitter documentation in the following links.

http://developers.facebook.com/docs/authentication/

https://dev.twitter.com/

Furthermore, Bitly (http://bitly.com/), a url shortening service, is used to publish your content, so it's necessary to get a Bitly account and obtain the access key also in this case.

A new configuration panel is added to the configuration area of Plone where you will be able to set the tokens and secret keys for Facebook, Twitter and Bitly.


Important: If you are testing this product in a non-public network, it's necessary to add a fake domain to your hosts file. Ex: 127.0.0.1       example.com

This is because the bitly service will try to reach the portal where this product has been installed, and if it doesn't you will get an error, so you must use something like http://example.com:8080/Plone

Permissions
Site Managers and content editors are able to publish the content to Twitter and Facebook.